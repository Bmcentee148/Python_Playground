# This will read in values given by the user and then display its average.
# author: 	Brian McEntee

def compute_average(values) :
	total = 0
	for val in values:
		total += val
	return float(total) / len(values)

print "Enter numbers one at a time. When finished enter 'd'"

curr_val = raw_input()
values = []

while(curr_val != 'd') :
	values.append(float(curr_val))
	curr_val = raw_input()

print "The average of these values is %.2f" % compute_average(values)



