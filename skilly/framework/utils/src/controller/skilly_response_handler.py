import datetime

'''

# Class to manage the http responses
    # Parameters:
        http (dict): {"code": 100, "success": True}
        response (dict): {}
        
    # Returns:
        func(schemaName, body)
        Response(400)
'''


class ResponseHandler:
    HTTP_CONTINUE = lambda self, message=None: {**self.__o, "code": 100, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 100, "success": True}
    SWITCHING_PROTOCOLS = lambda self, message=None: {**self.__o, "code": 101, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 101, "success": True}
    OK = lambda self, message=None: {**self.__o, "code": 200, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 200, "success": True}
    CREATED = lambda self, message=None: {**self.__o, "code": 201, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 201, "success": True}
    ACCEPTED = lambda self, message=None: {**self.__o, "code": 202, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 202, "success": True}
    NON_AUTHORITATIVE_INFORMATION = lambda self, message=None: {**self.__o, "code": 203, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 203, "success": True}
    NO_CONTENT = lambda self, message=None: {**self.__o, "code": 204, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 204, "success": True}
    RESET_CONTENT = lambda self, message=None: {**self.__o, "code": 205, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 205, "success": True}
    PARTIAL_CONTENT = lambda self, message=None: {**self.__o, "code": 206, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 206, "success": True}
    MULTI_STATUS = lambda self, message=None: {**self.__o, "code": 207, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 207, "success": True}
    MULTIPLE_CHOICES = lambda self, message=None: {**self.__o, "code": 300, "success": False, "message": message}\
        if message is not None else {**self.__o, "code": 300, "success": False}
    MOVED_PERMANENTLY = lambda self, message=None: {**self.__o, "code": 301, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 301, "success": False}
    FOUND = lambda self, message=None: {**self.__o, "code": 302, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 302, "success": False}
    SEE_OTHER = lambda self, message=None: {**self.__o, "code": 303, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 303, "success": False}
    NOT_MODIFIED = lambda self, message=None: {**self.__o, "code": 304, "success": True, "message": message} \
        if message is not None else {**self.__o, "code": 304, "success": True}
    USE_PROXY = lambda self, message=None: {**self.__o, "code": 305, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 305, "success": False}
    TEMPORARY_REDIRECT = lambda self, message=None: {**self.__o, "code": 307, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 307, "success": False}
    PERMANENT_REDIRECT = lambda self, message=None: {**self.__o, "code": 308, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 308, "success": False}
    BAD_REQUEST = lambda self, message=None: {**self.__o, "code": 400, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 400, "success": False}
    UNAUTHORIZED = lambda self, message=None: {**self.__o, "code": 401, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 401, "success": False}
    PAYMENT_REQUIRED = lambda self, message=None: {**self.__o, "code": 402, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 402, "success": False}
    FORBIDDEN = lambda self, message=None: {**self.__o, "code": 403, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 403, "success": False}
    NOT_FOUND = lambda self, message=None: {**self.__o, "code": 404, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 404, "success": False}
    METHOD_NOT_ALLOWED = lambda self, message=None: {**self.__o, "code": 405, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 405, "success": False}
    NOT_ACCEPTABLE = lambda self, message=None: {**self.__o, "code": 406, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 406, "success": False}
    PROXY_AUTHENTICATION_REQUIRED = lambda self, message=None: {**self.__o, "code": 407, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 407, "success": False}
    REQUEST_TIMEOUT = lambda self, message=None: {**self.__o, "code": 408, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 408, "success": False}
    CONFLICT = lambda self, message=None: {**self.__o, "code": 409, "success": False, "message": message}\
        if message is not None else {**self.__o, "code": 409, "success": False}
    GONE = lambda self, message=None: {**self.__o, "code": 410, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 410, "success": False}
    LENGTH_REQUIRED = lambda self, message=None: {**self.__o, "code": 411, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 411, "success": False}
    PRECONDITION_FAILED = lambda self, message=None: {**self.__o, "code": 412, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 412, "success": False}
    PAYLOAD_TOO_LARGE = lambda self, message=None: {**self.__o, "code": 413, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 413, "success": False}
    URI_TOO_LONG = lambda self, message=None: {**self.__o, "code": 414, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 414, "success": False}
    UNSUPPORTED_MEDIA_TYPE = lambda self, message=None: {**self.__o, "code": 415, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 415, "success": False}
    RANGE_NOT_SATISFIABLE = lambda self, message=None: {**self.__o, "code": 416, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 416, "success": False}
    EXPECTATION_FAILED = lambda self, message=None: {**self.__o, "code": 417, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 417, "success": False}
    MISDIRECTED_REQUEST = lambda self, message=None: {**self.__o, "code": 421, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 421, "success": False}
    UNPROCESSABLE_ENTITY = lambda self, message=None: {**self.__o, "code": 422, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 422, "success": False}
    LOCKED = lambda self, message=None: {**self.__o, "code": 423, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 423, "success": False}
    FAILED_DEPENDENCY = lambda self, message=None: {**self.__o, "code": 424, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 424, "success": False}
    TOO_EARLY = lambda self, message=None: {**self.__o, "code": 425, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 425, "success": False}
    UPGRADE_REQUIRED = lambda self, message=None: {**self.__o, "code": 426, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 426, "success": False}
    PRECONDITION_REQUIRED = lambda self, message=None: {**self.__o, "code": 428, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 428, "success": False}
    TOO_MANY_REQUESTS = lambda self, message=None: {**self.__o, "code": 429, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 429, "success": False}
    REQUEST_HEADER_FIELDS_TOO_LARGE = lambda self, message=None: {**self.__o, "code": 431, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 431, "success": False}
    UNAVAILABLE_FOR_LEGAL_REASONS = lambda self, message=None: {**self.__o, "code": 451, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 451, "success": False}
    INTERNAL_SERVER_ERROR = lambda self, message=None: {**self.__o, "code": 500, "success": False, "message": message} \
        if message is not None else {**self.__o, "code": 500, "success": False}

    __o = {
        "timestamp": ""
    }

    def __init__(self, obj=None):
        if obj is not None:
            self.__o['response'] = obj
        else:
            if "response" in self.__o:
                self.__o.__delitem__("response")
        self.__o['timestamp'] = datetime.datetime.timestamp(datetime.datetime.now())

    @classmethod
    def send(cls, response=None):
        return ResponseHandler(obj=response)
