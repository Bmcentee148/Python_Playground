# This will show examples of using pythons built in Set data structure. 

basket = ["apple", "pear", "banana", "apple", "pear", "orange"]
fruits = set(basket) # create a set of fruits without duplicates
print fruits

print 'orange' in fruits # fast membership testing
print 'crabs' in fruits 

a = set('abracadabra')
b = set('alacazam')
print a - b # letters in a but not in b
print a | b # letters in either a or b -> union
print a & b # letters in both a and b -> instersection
print a ^ b # letters in either a or b but not both -> exclusive or

c = {x for x in a if x not in 'abc'} # create set using set comprehension
print c
