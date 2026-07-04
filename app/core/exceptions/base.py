class AppException(Exception):

    status_code = 400
    message = "Application Error"

    def __init__(self, message=None):

        if message:
            self.message = message
