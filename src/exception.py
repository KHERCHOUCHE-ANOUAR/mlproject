import sys
import logger


def error_message_detail(error, context:sys):
    """
    Extracts the error message from an exception and formats it with context.
    """
    _, _, exc_tb = context.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that formats the error message with context.
    """
    def __init__(self, error, context:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, context)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        raise ValueError("An example error")
    except Exception as e:
        exc = CustomException(e, sys)
        logger.logging.info(exc)