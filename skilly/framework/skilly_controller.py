import json
from functools import wraps
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# Define a dictionary to store the routes
routes = {}


# Decorator to register route paths and methods
def routee(path, method):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        routes[path] = (method, wrapper)
        return wrapper

    return decorator


# Custom request handler
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        finalRoute = routes.get(getSchema(self.path))
        if finalRoute is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        method, handler = finalRoute
        if method != "GET":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(b"Method Not Allowed")
            return

        response = handler(self)
        self.send_response(response['code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response['data']).encode("utf-8"))

    def do_POST(self):
        route = routes.get(self.path.split("?")[0])
        if route is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        method, handler = route
        if method != "POST":
            self.send_response(405)
            self.end_headers()
            self.wfile.write(b"Method Not Allowed")
            return

        response = handler(self)
        self.send_response(response['code'])
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(json.dumps(response['data']).encode("utf-8"))


# Start the server
def run_server():
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()


def args(request):
    return parse_qs(urlparse(request.path).query)


def pathVars(request):
    schema = getSchema(request.path)
    counter = 0
    obj = {}
    for pathVariable in schema.split("/"):
        if pathVariable.startswith("{"):
            obj[pathVariable.replace("{", "").replace("}", "")] = getNumber(counter, request.path.split("?")[0])
            counter += 1
    return obj


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
