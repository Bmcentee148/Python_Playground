import time
from time import localtime
from bm_cust_exc import CaseyThursdayError
date = localtime()
if date.tm_wday == 4 :
    try:
        raise CaseyThursdayError("So much poop on the floor.")
    except CaseyThursdayError as e :
        print "Error: Looks like its Thursday again.", e.the_problem
else :
    print "You're damn luck sir... it isn't Thursday yet."