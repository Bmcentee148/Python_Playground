# Practicing creating custom exceptions for use in a module or program

class Error(Exception) :
    """A base class for custom exception classes.

    All custom exceptions should inherit from this class.
    """
    pass

class TransitionError(Error) :
    """An error for failing to properly transition from one state to another. 

    Attributes:
        prev_state -- the state transitioning from
        next_state -- the state transitioning to
        msg -- an explanation of why the exception occured
    """
    def __init__(self, prev_state, next_state, msg) :
        self.prev_state = prev_state
        self.next_state = next_state
        self.msg = msg

    def __str__(self) :
        return repr(self.msg)

def might_throw(prev, next) :
    if next < 0 :
        raise TransitionError(prev, next, 
            "Can't transition to negative number. %s -> %s" %(prev,next))
    else :
        print "Transitioning from", prev, "to", next

def will_throw(p_state, n_state) :
    try :
        raise TransitionError(p_state, n_state, "failed tansition")
    except TransitionError as e :
        print e.msg
        raise

def main() :
    # TEST CODE FOR CUSTOM EXCEPTION CLASSES
    # try :
    #     might_throw(1,2)
    #     might_throw(-2,30)
    #     might_throw(10,-2)
    # except TransitionError as e :
    #     print "Error while trasitioning :", e.msg
    will_throw("before","after")
    print "program running after error"
if __name__ == "__main__" :
    main()