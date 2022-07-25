import logging

from src.utils.httpStatus import HttpStatus
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError


class GeneralErrorHandler:
    def __init__(self, exception: Exception, model: str):
        self.exception = exception
        self.model = model

    @property
    def throw_err(self):

        logging.warning(self.exception)

        if type(self.exception) == IntegrityError:
            return {"message": f"{self.model} already exists"}, HttpStatus.INTEGRITY_ERROR
        if type(self.exception) == ValidationError:
            return {"message": str(self.exception)}, HttpStatus.VALIDATION_ERROR
        if type(self.exception) == TypeError:
            return {"message": "An error occurred. Please try again"}, HttpStatus.TYPE_ERROR
        else:
            return {"message": "A server error occurred. Contact Admin"}, HttpStatus.GENERAL_ERROR

