import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

from skilly.framework.utils.src.controller.skilly_response_handler import ResponseHandler

'''

# Variable that keeps stored all the active endpoints of the server
    # Parameters:
        -
    # Returns:
        -
'''

routes = {}

'''

# Class to manage the http requests
    # Parameters:
        -
    # Returns:
        -
'''


class RequestHandler(BaseHTTPRequestHandler):
    """

    # Returns None, handle the get requests and manage the errors
        # Parameters:
            -
        # Returns:
            -
    """

    def do_GET(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(
                json.dumps(ResponseHandler.send().NOT_FOUND("This route doesn't exist.")).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "GET":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(
                json.dumps(ResponseHandler.send().METHOD_NOT_ALLOWED("This method is not allowed.")).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['code'])
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    """

    # Returns None, handle the delete requests and manage the errors
        # Parameters:
            -
        # Returns:
            -
    """

    def do_DELETE(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler.send().NOT_FOUND("This route doesn't exist.")).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "DELETE":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler.send().METHOD_NOT_ALLOWED("This method is not allowed.")).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    """

    # Returns None, handle the put requests and manage the errors
        # Parameters:
            -
        # Returns:
            -
    """

    def do_PUT(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler.send().NOT_FOUND("This route doesn't exist.")).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "PUT":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler.send().METHOD_NOT_ALLOWED("This method is not allowed.")).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    """

    # Returns None, handle the post requests and manage the errors
        # Parameters:
            -
        # Returns:
            -
    """

    def do_POST(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler.send().NOT_FOUND("This route doesn't exist.")).encode("utf-8"))
            return

        method, handler = finalRoute
        if method != "POST":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(json.dumps(ResponseHandler.send().METHOD_NOT_ALLOWED("This method is not allowed.")).encode("utf-8"))
            return

        response = handler(self)
        self.send_response(response['code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    """

    # Returns an object full of query params or just a query param
        # Parameters:
            query: (str) -> "name"
        # Returns:
            object: (dict) -> { "name": "Ok", "age": "14" } |
            value: (str) -> "Ok"
    """

    def query(self, query=None):
        return parse_qs(urlparse(self.path).query) if query is None else parse_qs(urlparse(self.path).query)[query][0]

    """

    # Returns a string representing the jwt token
        # Parameters:
            -
        # Returns:
            value: (str) -> "ey....."
    """

    def token(self):
        return self.headers.get('Authorization').split(' ')[1]

    """

    # Returns an object full of path variables or just a path variable
        # Parameters:
            pathName: (str) -> "name"
        # Returns:
            object: (dict) -> { "date": "24", "age": "14" } |
            value: (str) -> "24"
    """

    def variables(self, pathName=None):
        schema = getSchema(self.path)
        counter = 0
        obj = {}
        for pathVariable in schema.split("/"):
            if pathVariable.startswith("{"):
                obj[pathVariable.replace("{", "").replace("}", "")] = getNumber(counter, self.path.split("?")[0])
                counter += 1
        return obj if pathName is None else obj[pathName]

    """

    # Returns an object full of query params or just a query param
        # Parameters:
            -
        # Returns:
            object: (dict) -> { "name": "Ok", "age": "14" }
    """

    def body(self):
        return json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode("utf-8"))


def run_server(ip="localhost", port=8080):
    server_address = (ip, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print("[skilly.server] -> Skilly server running on http://" + ip + ":" + str(port))
    httpd.serve_forever()


"""

# Returns the param which is at the position: number of the string
# Example: get/2/4
    # Parameters:
        number: (int) -> 1
    # Returns:
        value: (str) -> 4
"""


def getNumber(number, request):
    thisCounter = 0
    for part in request.split("/"):
        if part.isnumeric():
            if thisCounter == number:
                return part
            thisCounter += 1


"""

# Returns the schema of the given path
    # Parameters:
        path: (str) -> "get/4"
    # Returns:
        value: (str) -> "get/{userId}"
"""


def getSchema(path):
    workingPath = path.split("?")[0]
    finalRoute = workingPath
    done = False
    for route in routes:
        if len(route.split("/")) == len(workingPath.split("/")):
            for i in range(len(workingPath.split("/"))):
                if route.split("/")[i].startswith("{") \
                        and workingPath.split("/")[i].isnumeric() \
                        or route.split("/")[i] != "" \
                        and route.split("/")[i] == workingPath.split("/")[i]:
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
