import sys
from typing import Any

def error_message_detail(error: Exception, error_detail: Any) -> str:
    """
    Build a detailed error message using the traceback info available
    from the provided error_detail (typically the sys module).
    """
    _, _, exc_tb = error_detail.exc_info()
    # If traceback is missing (defensive), return a simple message
    if exc_tb is None:
        return f"Error message: [{str(error)}]"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in the Python script: [{file_name}] "
        f"at line: [{line_number}] -> Error message: [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    """
    Custom exception that wraps another exception and stores a
    detailed, formatted message produced by error_message_detail.
    """

    def __init__(self, error: Exception, error_detail: Any):
        # Build the detailed message using the helper function
        detailed_message = error_message_detail(error, error_detail)
        # Initialize base Exception with the detailed message
        super().__init__(detailed_message)
        # Also keep the message on the instance for easy access
        self.error_message = detailed_message

    def __str__(self) -> str:
        return self.error_message