class ErrorModel(object):
    def __init__(self,
    stack_trace: str, 
    error_message: str,
    inner_error_message: str = None,
    optional_data: str = None) -> None:
        self.stack_trace: str = stack_trace
        self.error_message: str = error_message
        self.inner_error_message: str = inner_error_message
        self.optional_data: str = optional_data
