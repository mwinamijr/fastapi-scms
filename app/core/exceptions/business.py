from fastapi import status

from .base import AppException


class ResourceNotFound(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Resource not found."


class DuplicateResource(AppException):
    status_code = status.HTTP_409_CONFLICT
    message = "Resource already exists."


class InvalidOperation(AppException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Invalid operation."


class BusinessRuleViolation(AppException):
    status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
    message = "Business rule violated."
