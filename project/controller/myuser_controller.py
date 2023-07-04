from urllib.parse import urlparse, parse_qs

from skilly.framework.skilly_controller import run_server, routee, args, pathVars


# Define route handler functions
@routee("/{userId}/{aa}/{bb}", "GET")
def home(request):
    return {"code": 200, "data": {"query": args(request), "path_var": pathVars(request)}}


@routee("/greet/{aa}", "GET")
def greet(request):
    return {"code": 200, "data": {"okk": parse_qs(urlparse(request.path).query)}}


@routee("/params", "GET")
def params(request):
    return {"code": 200, "data": {"ok": parse_qs(urlparse(request.path).query)}}

run_server()
