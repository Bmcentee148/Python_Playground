# Fibonacci Numbers Module

def fibl(max_num) :
    """Returns a list of the fibonacci sequence up to a maximum value

    Parameters:
        max_num -- the max allowed number in the returned fibonacci sequence
    """    
    a, b = 0, 1
    result = []
    while a <= max_num :
        result.append(a)
        a, b = b, a + b
    return result

def fibp(max_num) :
    """Prints the fibonacci sequence up to a maximum value.

    Parameters:
        max_num -- the max allowed number in the fibonacci sequence
    """
    a, b = 0 , 1
    while a <= max_num :
        print a,
        a, b = b, a + b

if __name__ == "__main__" :
    import sys
    try:
        fibp(int(sys.argv[1]))
    except ValueError as e :
        print e
        print "usage: python fibo.py <integer>"
    