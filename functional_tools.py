# This will utilize built in functions filter(), map(), and reduce(). They are
# important for "functional programming".


def f(x) :
    return (x % 5 == 0) or (x % 3 == 0)

# Print list of digits in range of 2 through 24 that are either divisible by 5  
# or divisible by 3
print filter(f, range(2,25))

def cube(x) :
    return x*x*x

# Print a list that contains the cubes of the integers 1 through 10
print map(cube, range(1,11))

def add(x,y) :
    return x + y

# Print the sum of the integers 1 through 10
print reduce(add, range(1,11))

def sum(seq) :
    def add(x,y) : return x + y
    return reduce(add, seq, 0)

print sum(range(1,11))
print sum([])