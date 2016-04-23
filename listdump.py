# Empty a list

l = [1, 2, 3]
print l

index = 0
while l :
    print l.pop(index)
    print l
print "List should be empty"
print l
if not l:
    print "Success!"
else :
    print "Something is wrong"

    

