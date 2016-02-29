# This will flip a 'coin' the desired number of times and count the number of
# occurrences of both Heads and Tails

import random
from sys import argv
script_name, num_flips, num_experiments = argv
num_flips = int(num_flips)
num_experiments = int(num_experiments)

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

def print_results(results) :
    experiment_number = 1
    for experiment in results :
        print "\nExperiment #%d:" % experiment_number
        print "---------------"
        print "# Heads: %d" % experiment[HEADS]
        print "# Tails: %d" % experiment[TAILS]
        experiment_number += 1


# Script
print "Number of experiments: %d" % num_experiments
print "Number of flips per experiment: %d" % num_flips
experiment_results = []

for i in range(num_experiments) :
    experiment_results.append(flip_coin(num_flips))

print_results(experiment_results)




