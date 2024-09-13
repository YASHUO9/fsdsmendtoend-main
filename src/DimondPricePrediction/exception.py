import sys


class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        """ custom exception class to log error message, line number and file name"""
        
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()  # get the exception traceback or object
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        """string representation of custom exception"""
        
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
        
    

if __name__ == "__main__":
    
    """ testing custom exception"""
    try:
        
        a=1/0
        #zero division error
    
    except Exception as e:
        raise customexception(e,sys)
        