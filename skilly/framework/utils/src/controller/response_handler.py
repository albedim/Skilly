import datetime


class ResponseHandler:

    HTTP_CONTINUE = {"code": 100, "success": True}
    HTTP_SWITCHING_PROTOCOLS = {"code": 101, "success": True}
    HTTP_OK = {"code": 200, "success": True}
    HTTP_CREATED = {"code": 201, "success": True}
    HTTP_ACCEPTED = {"code": 202, "success": True}
    HTTP_NON_AUTHORITATIVE_INFORMATION = {"code": 203, "success": True}
    HTTP_NO_CONTENT = {"code": 204, "success": True}
    HTTP_RESET_CONTENT = {"code": 205, "success": True}
    HTTP_PARTIAL_CONTENT = {"code": 206, "success": True}
    HTTP_MULTI_STATUS = {"code": 207, "success": True}
    HTTP_MULTIPLE_CHOICES = {"code": 300, "success": False}
    HTTP_MOVED_PERMANENTLY = {"code": 301, "success": False}
    HTTP_FOUND = {"code": 302, "success": False}
    HTTP_SEE_OTHER = {"code": 303, "success": False}
    HTTP_NOT_MODIFIED = {"code": 304, "success": True}
    HTTP_USE_PROXY = {"code": 305, "success": False}
    HTTP_TEMPORARY_REDIRECT = {"code": 307, "success": False}
    HTTP_PERMANENT_REDIRECT = {"code": 308, "success": False}
    HTTP_BAD_REQUEST = {"code": 400, "success": False}
    HTTP_UNAUTHORIZED = {"code": 401, "success": False}
    HTTP_PAYMENT_REQUIRED = {"code": 402, "success": False}
    HTTP_FORBIDDEN = {"code": 403, "success": False}
    HTTP_NOT_FOUND = {"code": 404, "success": False}
    HTTP_METHOD_NOT_ALLOWED = {"code": 405, "success": False}
    HTTP_NOT_ACCEPTABLE = {"code": 406, "success": False}
    HTTP_PROXY_AUTHENTICATION_REQUIRED = {"code": 407, "success": False}
    HTTP_REQUEST_TIMEOUT = {"code": 408, "success": False}
    HTTP_CONFLICT = {"code": 409, "success": False}
    HTTP_GONE = {"code": 410, "success": False}
    HTTP_LENGTH_REQUIRED = {"code": 411, "success": False}
    HTTP_PRECONDITION_FAILED = {"code": 412, "success": False}
    HTTP_PAYLOAD_TOO_LARGE = {"code": 413, "success": False}
    HTTP_URI_TOO_LONG = {"code": 414, "success": False}
    HTTP_UNSUPPORTED_MEDIA_TYPE = {"code": 415, "success": False}
    HTTP_RANGE_NOT_SATISFIABLE = {"code": 416, "success": False}
    HTTP_EXPECTATION_FAILED = {"code": 417, "success": False}
    HTTP_MISDIRECTED_REQUEST = {"code": 421, "success": False}
    HTTP_UNPROCESSABLE_ENTITY = {"code": 422, "success": False}
    HTTP_LOCKED = {"code": 423, "success": False}
    HTTP_FAILED_DEPENDENCY = {"code": 424, "success": False}
    HTTP_TOO_EARLY = {"code": 425, "success": False}
    HTTP_UPGRADE_REQUIRED = {"code": 426, "success": False}
    HTTP_PRECONDITION_REQUIRED = {"code": 428, "success": False}
    HTTP_TOO_MANY_REQUESTS = {"code": 429, "success": False}
    HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE = {"code": 431, "success": False}
    HTTP_UNAVAILABLE_FOR_LEGAL_REASONS = {"code": 451, "success": False}
    HTTP_INTERNAL_SERVER_ERROR = {"code": 500, "success": False}

    __o = {
        "success": False,
        "status_code": 0,
        "response": "",
        "timestamp": ""
    }

    def __init__(self, http=None, response=None, obj=None):
        if obj is None:
            self.__o['status_code'] = http['code']
            self.__o['success'] = http['success']
            self.__o['response'] = response
            self.__o['timestamp'] = datetime.datetime.timestamp(datetime.datetime.now())
        else:
            self.__o = obj

    def setMessage(self, message):
        if self.__o['success']:
            self.__o['message'] = message
        else:
            self.__o['error'] = message
        return ResponseHandler(obj=self.__o)

    def send(self):
        return self.__o

