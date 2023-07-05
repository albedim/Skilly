import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from skilly.framework.utils.src.controller.response_handler import ResponseHandler


routes = {}


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_NOT_FOUND,
                response={}).setMessage("This route doesn't exist.").send()).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "GET":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_METHOD_NOT_ALLOWED,
                response={}).setMessage("This method is not allowed").send()).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['status_code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_DELETE(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_NOT_FOUND,
                response={}).setMessage("This route doesn't exist.").send()).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "DELETE":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_METHOD_NOT_ALLOWED,
                response={}).setMessage("This method is not allowed").send()).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['status_code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_PUT(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_NOT_FOUND,
                response={}).setMessage("This route doesn't exist.").send()).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "PUT":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_METHOD_NOT_ALLOWED,
                response={}).setMessage("This method is not allowed").send()).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['status_code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_NOT_FOUND,
                response={}).setMessage("This route doesn't exist.").send()).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "POST":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler(
                http=ResponseHandler.HTTP_METHOD_NOT_ALLOWED,
                response={}).setMessage("This method is not allowed").send()).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['status_code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def query(self, query=None):
        return parse_qs(urlparse(self.path).query) if query is None else parse_qs(urlparse(self.path).query)[query][0]

    def variables(self, pathName=None):
        schema = getSchema(self.path)
        counter = 0
        obj = {}
        for pathVariable in schema.split("/"):
            if pathVariable.startswith("{"):
                obj[pathVariable.replace("{", "").replace("}", "")] = getNumber(counter, self.path.split("?")[0])
                counter += 1
        return obj if pathName is None else obj[pathName]

    def body(self):
        return json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode("utf-8"))


# Start the server
def run_server():
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()


def getNumber(number, request):
    thisCounter = 0
    for part in request.split("/"):
        if part.isnumeric():
            if thisCounter == number:
                return part
            thisCounter += 1


def getSchema(path):
    workingPath = path.split("?")[0]
    finalRoute = workingPath
    done = False
    for route in routes:
        if len(route.split("/")) == len(workingPath.split("/")):
            for i in range(len(workingPath.split("/"))):
                a = route.split("/")[i]
                b = workingPath.split("/")[i]
                if route.split("/")[i].startswith("{") and workingPath.split("/")[i].isnumeric() \
                        or route.split("/")[i] != "" and route.split("/")[i] == workingPath.split("/")[i]:
                    if i == len(workingPath.split("/")) - 1:
                        done = True
                        finalRoute = route
                        break
                else:
                    if route.split("/")[i] != "":
                        break
        if done:
            break
    return finalRoute
