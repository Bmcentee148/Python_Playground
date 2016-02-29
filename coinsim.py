# This will flip a 'coin' the desired number of times and count the number of
# occurrences of both Heads and Tails

import random
from sys import argv
script_name, num_flips = argv

# Method Declarations
def flip_coin() :
	"""Return 0 for Heads or 1 for Tails at random """
	return int(random.random() * 2) 

# Defined Constants
HEADS = 0
TAILS = 1

# Script
num_flips = int(num_flips)
print "Number of flips: %d" % num_flips
face_freq = [0, 0] # initially 0 heads and 0 tails obtained

for i in range(num_flips):
	result = flip_coin()
	if result == HEADS :
		face_freq[HEADS] += 1
	elif result == TAILS :
		face_freq[TAILS] += 1
	else :
		print "Error: Unexpected Result From Coin Flip."

print "Results: ", face_freq


