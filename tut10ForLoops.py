# Many Object in Python are "iterable"
# ie, we can iterate overy element in the object
# such as every element in a list
# or every character in a string
# we can use for loops to execute a block of code for every iteration



mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    print('Cool!')

for num in mylist:
    if num % 2 == 0 :
        print(num)
    else:
        print(f'Odd number : {num}')

# Prints the sum at the end once
list_sum = 0
for num in mylist:
    list_sum=list_sum+num
print(list_sum)

# Prints the running total
list_sum = 0
for num in mylist:
    list_sum=list_sum+num
    print(list_sum)


my_string='Hello World'
for letter in my_string:
    print(letter)


for letter in 'Hello World':
    print(letter)

for gggg in 'Hello World':
    print(gggg)

# Using _ when not intended to use the variable
for _ in 'Hello World':
    print('Cool!')

tup = (1,2,3)

for item in tup:
    print(item)



my_list = [(1,2),(3,4),(5,6)]
print(len(my_list))


# returns
# (1, 2)
# (3, 4)
# (5, 6)
for item in my_list:
    print(item)

####### Tuple Unpacking
for (a,b) in my_list:
    print(a)
    print(b)

for (a,b) in my_list:
    print(a)

# () is optional
for a,b in my_list:
    print(b)

my_list = [(1,2,3),(5,6,7),(8,9,10)]

for a,b,c in my_list:
    print(b)
####### Tuple Unpacking

d = {'K1':1,'K2':2,'K3':3}

# prints only the keys
# K1
# K2
# K3
for item in d:
    print(item)



# Prints
#('K1', 1)
#('K2', 2)
#('K3', 3)
for item in d.items():
    print(item)


# we can use the tuple unpacking to take the values out
for key,value in d.items():
    print(value)

# we can also use the values() function to get the values out
for value in d.values():
    print(value)