from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError

from .base import AppException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Validation failed.",
                "errors": exc.errors(),
            },
        )

    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request, exc):

        message = "Database integrity error."

        error = str(exc.orig)

        if "duplicate key value" in error:

            if "users_email_key" in error:
                message = "Email already exists."

            elif "users_phone_key" in error:
                message = "Phone number already exists."

            elif "schools_code" in error:
                message = "School code already exists."

            else:
                message = "Duplicate record."

        elif "foreign key constraint" in error:
            message = "Referenced record does not exist."

        elif "not-null constraint" in error:
            message = "Required field is missing."

        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": message,
            },
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_handler(request, exc):

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Database error.",
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request, exc):

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal server error.",
            },
        )
