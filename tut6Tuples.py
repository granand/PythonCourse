# Tuples are very similar to Lists
# However the key difference is Tuples are immutable
# ie, Once an element is inside a tuple, it cannot be reassigned
# Tuples use parenthesis: (1,2,3)

t = (1,2,3)

my_list = [1,2,3]

# returns <class 'tuple'>
print(type(t))
# returns <class 'list'>
print(type(my_list))

# returns 3
print(len(t))

# Like lists we can mix objects inside a Tuple
t1 = ("one",2)

# Like list we can use index to print the first or last elements
# returns one - the first element
print(t1[0])
# returns 2 - the last element in the Tuple
print(t1[-1])

t = ('a','a','b')

# returns the number of times 'a' occurs in Tuple
# returns 2
t.count('a')

# returns 0  - returns the index of the first occurrence of the element
t.index('a')

# returns 2  - returns the index of the first occurrence of the element
t.index('b')


my_list = [1,2,3]
my_list[0]="NEW"
# returns ['NEW', 2, 3]
print(my_list)


t = (1,2,3)
# Throws Error - TypeError: 'tuple' object does not support item assignment
# t[0]='a'