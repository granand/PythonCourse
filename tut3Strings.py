# strings are ordered sequences, it means we can use indexing and slicing
# to grab sub-sections of the string
# index for string starts at zero

# character : h  e  l  l  o
# Index     : 0  1  2  3  4
# Reverse   : 0 -4 -3 -2 -1
# Index

# slicing    [start:stop:step]
################################
text='Hello World'
print(text)

print("Hello \nWorld")
print("Hello \tWorld")

print(len(text))

# returns H - char at position 0
print(text[0])

# returns r - char at position 8
print(text[8])

# returns l - char at position -2
print(text[-2])

# returns d - last character of a string
print(text[-1])

my_string = "abcdefghijk"

# returns cdefghijk - starting from poistion 2 return full string
print(my_string[2:])

# returns abc - upto position 3 but not 3
print(my_string[:3])

# returns empty - start from index and upto position 3 but not 3
print(my_string[3:3])

# returns de - start from index and upto position 5 but not 5
print(my_string[3:5])

# returns full string
print(my_string[::])

# returns acegik - step 2 - ie, strat at index 0 and step is 2. Default is 1
print(my_string[::2])

# returns ceg
print(my_string[2:7:2])

# reversing a string
print(my_string[-1::-1])

# below is the short way to reverse the string
print(my_string[::-1])

##################################
# Immutability
# Strings are immutable
name="Sam"
# we cannot run the below
#name[0]="P"

# concatenation
last_letters = name[1:]
print("P" + last_letters)

# prints ZZZZZZZZZZ
letter = "Z"
print(letter*10)

# built in string methods
x="Hello World"
print(x.upper())
print(x.lower())
print(x.split())
print(x.split("l"))

#######################################
# print formatting
# this avoids unneccessary concatenation

# outputs This is a string INSERTED
print('This is a string {}'.format('INSERTED'))

# prints The fox brown quick
print('The {} {} {}'.format('fox','brown','quick'))

# prints The brown fox quick
print('The {1} {0} {2}'.format('fox','brown','quick'))

# prints The fox fox fox
print('The {0} {0} {0}'.format('fox','brown','quick'))

# prints The quick brown fox
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

# prints The fox fox fox
print('The {f} {f} {f}'.format(f='fox',b='brown',q='quick'))

### float formatting
result = 100/777
# prints 0.1287001287001287
print(result)

# The result is 0.1287001287001287
print("The result is {r}".format(r=result))

# Float formatting is "{value:width.precision f}"
# The result is      0.129
print("The result is {r:10.3f}".format(r=result))

######
name = "Anand"
age = 3
# New in Python 3
# prints  Hello, his name is Anand
print(f'Hello, his name is {name}')

# prints Anand is 3 years old
print(f'{name} is {age} years old')
