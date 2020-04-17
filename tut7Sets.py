# Sets are unordered collections of Unique elements
# Meaning no duplicates

myset = set()
myset.add(1)

# returns {1}
print(myset)

myset.add(2)
myset.add(2)

# returns {1, 2}
print(myset)

#-------

mylist=[1,1,1,1,2,2,2,2,2,3,3,3,3,3]
# convert list to a set
new_set=set(mylist)
# returns {1, 2, 3}  -- Order is not Guranteed
print(new_set)
