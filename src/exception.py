# import sys
# from src.logger import logging

# def error_message_detail(error,error_detail:sys):
#     # (this tells us where exactly the error occurred
#     _,_,exc_tb=error_detail.exc_info()  
    
#     #This gets the name of the Python file where the error occurred.
#     file_name=exc_tb.tb_frame.f_code.co_filename
    
#     # exc_tb.tb_lineno: This gets the line number in the code where the error happened
#     # error_message: This combines the file name, line number, and the error message into a formatted string. For example:
#     # Error occured in python script name [setup.py] line number [20] error message[Invalid requirement: '']
#     # This helps in debugging and understanding where the error occurred.
#     # This information will help us to identify the exact line of code where the error occurred.
#     error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
#      file_name,exc_tb.tb_lineno,str(error))

#     return error_message

    

# class CustomException(Exception):
#     def __init__(self,error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
#     def __str__(self):
#         return self.error_message
    

import sys
from src.logger import logging

def format_error_message(exception, sys_info: sys):
    _, _, traceback_obj = sys_info.exc_info()
    script_name = traceback_obj.tb_frame.f_code.co_filename
    formatted_error_message = "Error occurred in python script name [{0}] at line number [{1}] with error message [{2}]".format(
        script_name, traceback_obj.tb_lineno, str(exception))

    return formatted_error_message


class CustomException(Exception):
    def __init__(self, exception_message, sys_info: sys):
        super().__init__(exception_message)
        self.detailed_error_message = format_error_message(exception_message, sys_info=sys_info)
    
    def __str__(self):
        return self.detailed_error_message
