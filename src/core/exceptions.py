"""Exceptions module."""


class BaseException(Exception):
    """Base exception class."""

    def __init__(self, message: str = "Internal Server Error") -> None:
        if message:
            self.message = message


class NotFoundException(BaseException):
    """Not found exception class."""

    message = "Not Found"
