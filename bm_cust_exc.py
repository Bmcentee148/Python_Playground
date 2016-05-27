class Error(Exception) :
    """Base class for custom exception classes."""
    pass

class InputError(Error) :
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg -- explanation of the error
    """ 
    def __init__(self,expr,msg) :
        self.expr = expr
        self.msg = msg

class HolyShitError(Error) :
    """Exception raised in the case all goes to hell.
        
    Attributes:
        msg -- Advice to the user on what to do now...
    """

    def __init__(self, msg) :
        self.msg = msg

class CaseyThursdayError(Error) :
    """Exception raised in the case of a thursday breakdown.
    
    Attributes:
        the_problem -- The reason why a breakdown has occurred this Thursday.
    """

    def __init__(self, the_problem) :
        self.the_problem = the_problem

    def __str__(self) :
        return repr(self.the_problem)

