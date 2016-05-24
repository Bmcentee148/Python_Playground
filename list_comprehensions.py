# This will provide examples using list comprehensions which are generally for
# making new lists by applying some operation on each item of another list or to
# create a subsequence of the original list that satisfy some condition

# Create a list containing all the squares of digits 1 through 5
squares = [x**2 for x in range(1,6)]
print squares

# Create all pairs (x,y) for values of 1 through 3 if they are not the same val
pairs = [(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y]
print pairs

# Create the same pairs as above using loops, which kinda sucks
combs = []

for x in [1,2,3] :
    for y in [1,2,3] :
        if x!=y :
            combs.append((x,y))

print combs

vect = [-4, -2, 0, 2, 4]
print vect
# Create new list containing doubles of each value in vect
vect_doubled = [x*2 for x in vect]
print vect_doubled
# Create new list containing only the positive values in vect
vect_nonneg = [x for x in vect if x >= 0]
print vect_nonneg
# Apply a function to each value in vect
vect_abs = [abs(x) for x in vect]
print vect_abs

fruits = ["banana   ", "pear  ", "orange "]
# Call a method on each element in fruits
fruits_stripped = [word.strip(" ") for word in fruits]
print fruits_stripped

# Create a list of 2-tuples like (number, square)
num_sqr = [(x, x**2) for x in range(1,5)]
print num_sqr

# Flatten a list of lists using 2 for statements in the comprehension
vects = [[1,2,3], [2,3,4], [3,4,5]]
flattened_vect = [x for elem in vects for x in elem]
print flattened_vect
