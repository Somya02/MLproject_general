import sys
import logging
##
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()   # the first two info we are not interested but the last would give us the file in which error occured etc.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}] line_number[{1}] error_message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

    
class Custom_Exception(Exception):
    def __init__(self, error_message,error_detail:sys): 
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_deatil=error_detail)
        
    def str(self):
        return self.error_message
    
# if __name__=="__main__":
    
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("DIvide by zero error")
#         raise Custom_Exception(e, sys)
        