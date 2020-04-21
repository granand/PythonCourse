#### Generator
# range function

# prints numbers from 0 through 9
for num in range(10):
    print(num)

# start and end range
# starts from 3 and up to 9 but not 10
for num in range(3,10):
    print(num)

# start and end range with step size
# prints even numbers
# prints 0,2,4,6 and 8
# if you need 10 to be printed then you need to put 11 as end range
for num in range(0,10,2):
    print(num)


print("=====")

# the below returns range(0, 10)
print(range(10))

# prints the list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# cast generator to a list
print(list(range(10)))

a = range(10)
# the below returns the generator range(0, 10)
print(a)
# cast generator to a list
# prints the list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(a))


###### Enumerate

# prints the below
# value at index 0 is a
# value at index 1 is b
# value at index 2 is c
# value at index 3 is d
# value at index 4 is e
index = 0
for letter in 'abcde':
    print('value at index {} is {}'.format(index,letter))
    index += 1


# prints
# a
# b
# c
# d
index = 0
word = 'abcde'
for letter in word:
    print(word[index])
    index += 1

## Instead of the above two we can use enumerate to avoid manually using index and incrementing it

# enumerate returns a tuple and we can use tuple unpacking
# (0, 'a')
# (1, 'b')
# (2, 'c')
word='abc'
for item in enumerate(word):
    print(item)

# we can use tuple unpacking to get index or the letter, whatever we want
word='abc'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

##########  zip function
###### amlmost of opposite  of enumerate
# the below prints
# (1, 'a')
# (2, 'b')
# (3, 'c')
mylist1= [1,2,3]
mylist2=['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)

# the below prints
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
mylist1= [1,2,3]
mylist2=['a','b','c']
mylist3=[100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)
# Note : If one list is larger, zip can go as far as the smallest list



# puts the zipped results in a list
# prints [(1, 'a'), (2, 'b'), (3, 'c')]
mylist1= [1,2,3]
mylist2=['a','b','c']
print(list(zip(mylist1,mylist2)))

############

# use in to check if something is in the list
# returns True
print(2 in [1,2,3])

# works in string as well
# returns True
print('a' in 'a world')

# works for keys in dictionaries
# returns True
print('mykey' in {'mykey':345})


d={'mykey':345}
# returns False
print(345 in d.keys())

d={'mykey':345}
# returns True
print(345 in d.values())


######
# min and max functions

list={1,4,3,2}
print(max(list))
print(min(list))

##############
# random library

from random import shuffle
mylist=[1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)
# prints the list in random shuffled order
print(mylist)

#######
from random import randint
# prints a random integer between the range passed
print(randint(0,100))

######
# input function
# input always treats input as a string
print(input('Enter a Number :'))
