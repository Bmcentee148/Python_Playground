# This will read in data from a text file then find the median and average
# author: Brian McEntee

from sys import argv
script, file_name = argv

def compute_average(values) :
	total = 0
	for val in values:
		total += val
	return float(total) / len(values)

def compute_median(values) :
	values.sort()
	median_index = len(values) * .5
	if(median_index.is_integer()) :
		median_value = compute_average(values[int(median_index) - 1 : int(median_index)+ 1])
	else :
		median_index = int(median_index) + 1
		median_value = values[median_index - 1]
	return median_value

data = open(file_name).read().split()
for i in range(len(data)) :
	data[i] = float(data[i])

print "Average: %f" % compute_average(data)
print "Median: %f" % compute_median(data)

