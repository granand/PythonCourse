# List Comprehensions are a unique way of quickly creating a list with Python
# If you find yourself using a loop along with .append() to create a list
# List comprehensions are a good alternative!

## Old Style
list = []
for x in 'Hello':
    list.append(x)
print(list)

## List Comprehension
list = [x for x in 'Hello']
print(list)

# returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist=[num for num in range(0,11)]
print(mylist)

# doing operations on top of it
# returns [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
mylist=[num**2 for num in range(0,11)]
print(mylist)

# another example with complex Arithmetic
celcius = [0,10,20,39]

farenheit = [ ((9/5)*x+32) for x in celcius]
print(farenheit)

# Using If conditions along with it
# returns [0, 2, 4, 6, 8, 10]
mylist=[num for num in range(0,11) if num%2 == 0]
print(mylist)

## we can use if else but that changes the order

# prints [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]
mylist=[num if num%2 == 0 else 'ODD' for num in range(0,11) ]
print(mylist)

## Nested loops in traditional way
mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
# prints [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]
print(mylist)

## Nested loops in List Comprehension
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
# prints [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]
print(mylist)