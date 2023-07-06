class RouteHandler:

    def __init__(self, route):
        self.route = "/api/v1/" + route

    def new(self, endpoint):
        return self.route + endpoint
