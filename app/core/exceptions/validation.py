# validation.py

from fastapi import status

from .base import AppException


class ValidationException(AppException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    message = "Validation failed."
