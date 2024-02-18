from .base import DomainException


class NotFound(DomainException):
    def __init__(self, message: str, source: str = ""):
        super().__init__(404, message, source)
