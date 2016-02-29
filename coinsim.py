# This will flip a 'coin' the desired number of times and count the number of
# occurrences of both Heads and Tails

import random
from sys import argv
script_name, num_flips = argv
num_flips = int(num_flips)

# Defined Constants
HEADS = 0
TAILS = 1

# Method Declarations
def flip_coin(num_flips) :
    """Flips the coin given number of times and returns the results."""
    face_freq = [0, 0] # initially 0 heads and 0 tails obtained

    for i in range(num_flips) :
        result = int(random.random() * 2)
        if result == HEADS :
            face_freq[HEADS] += 1
        elif result == TAILS :
            face_freq[TAILS] += 1
        else :
            print "Error: Unexpected Flip Value."

    return face_freq


# Script
print "Number of flips: %d" % num_flips
results = flip_coin(num_flips)
print "Results: ", results



