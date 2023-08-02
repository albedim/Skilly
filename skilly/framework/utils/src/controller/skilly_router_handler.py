class RouteHandler:

    def __init__(self, route):
        self.route = "/api/v1/" + route

    def new(self, endpoint):
        return self.route + endpoint

    @classmethod
    def GET(cls):
        return "GET"

    @classmethod
    def PUT(cls):
        return "PUT"

    @classmethod
    def POST(cls):
        return "POST"

    @classmethod
    def DELETE(cls):
        return "DELETE"
