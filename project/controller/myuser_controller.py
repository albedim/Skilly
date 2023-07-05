from urllib.parse import urlparse, parse_qs

from project.service.service import MyUserService
from skilly.framework.server.src.decorators import route


# Define route handler functions
@route("/get", "GET")
def home(request):
    return MyUserService.getAllUsers()


@route("/removeAll", "DELETE")
def home(request):
    return MyUserService.removeAll()


@route("/update/{userId}", "PUT")
def home(request):
    return MyUserService.update(request.variables("userId"), request.query("name"))


@route("/add", "POST")
def home(request):
    return MyUserService.add(request.body())


@route("/get/{userId}", "GET")
def getUser(request):
    return MyUserService.getUserById(request.variables("userId"))

