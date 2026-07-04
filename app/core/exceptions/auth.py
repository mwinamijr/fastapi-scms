# auth.py

from fastapi import status

from .base import AppException


class InvalidCredentials(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Invalid username or password."


class InvalidToken(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Invalid access token."


class TokenExpired(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Access token has expired."


class PermissionDenied(AppException):
    status_code = status.HTTP_403_FORBIDDEN
    message = "Permission denied."
