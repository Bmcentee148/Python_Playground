# This will read in data from a text file then find the median and average
# author: Brian McEntee

from sys import argv
script, file_name = argv

def compute_average(values) :
	""" Compute the average, or mean, of a list of numbers.

		@type compute_average: list
		@param values: A list of numbers

		@rtype: float
		@return: Returns the statistical average of a list of numbers 
	"""
	total = 0.0
	for val in values:
		total += val
	return total / len(values)
# end compute_average(..)

def compute_median(values) :
	""" Compute and return the median of a list of possibly unsorted numbers.
		
		@type values: list
		@param values: A list of numbers to compute median of

		@rtype: float or int
		@return: Returns the statistical median of a list of numbers 
	"""
	values.sort()
	median_index = ( len(values) * .5 ) - 1
	if(median_index.is_integer()) :
		median_value = compute_average(
			values[int(median_index): int(median_index)+ 2])
	else :
		median_index = int(median_index)
		median_value = values[median_index]
	return median_value
#end compute_median(..)

def compute_variance(values) :
	""" Compute and return the variance in the list of numbers

		@type values: list
		@param values: A list of the data to get variance of

		@rtype: float
		@return: The statistical variance of the given data
	"""
	average = compute_average(values)
	sqr_diff_sum = 0.0
	for x in values :
		sqr_diff_sum += ((x - average) * (x - average))
	variance = sqr_diff_sum / (len(values) - 1) # use unbiased estimator
	return variance
# end compute_variance(..)

def get_data() :
	data = open(file_name).read().split()
	for i in range(len(data)) :
		data[i] = float(data[i])
	return data
# end get_data()

#Script
input_data = get_data()
print "Average: %f" % compute_average(input_data)
print "Median: %f" % compute_median(input_data)
print "Variance: %f" % compute_variance(input_data)

