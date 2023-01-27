from data_access.data_stores.sql.query_handlers.logging import LoggingQueryHandler
from core.data_models.error import ErrorModel

class Logger(object):

    def __init__(self, query_handler: LoggingQueryHandler) -> None:
        self.__query_handler: LoggingQueryHandler = query_handler

    def log_error(self, error: ErrorModel) -> None:
        self.__query_handler.log_error(error.stack_trace, 
        error.error_message, 
        error.inner_error_message,
        error.optional_data)

        return
