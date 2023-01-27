from datetime import datetime
from data_access.data_stores.sql.repositories.write import WriteRepository

class LoggingQueryHandler(object):

    def __init__(self, write_repository: WriteRepository) -> None:
        self.__write_repository: WriteRepository = write_repository

    def log_error(self, 
    stack_trace: str, 
    error_message: str,
    inner_error_message: str = None,
    optional_data: str = None) -> None:
        sql: str = self.__get_error_query(stack_trace, 
            error_message,
            inner_error_message,
            optional_data)

        self.__write_repository.write(sql)

        return
    
    def __get_error_query(self, 
    stack_trace: str, 
    error_message: str,
    inner_error_message: str,
    optional_data: str) -> str:
        return '''
            INSERT INTO 
                public.error(stack_trace, error_message, inner_error_message, optional_data, created_date)
            VALUES('{0}', '{1}', '{2}', '{3}', '{4}')'''.format(
                stack_trace.replace("'", "`").replace('"', '`'), 
                (error_message or '').replace("'", "`").replace('"', '`'), 
                (inner_error_message or '').replace("'", "`").replace('"', '`'),
                (optional_data or '').replace("'", "`").replace('"', '`'),
                datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            )
