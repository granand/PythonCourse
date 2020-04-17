# Variables cannot
#  - start with a number
#  - cannot have space in-between
#  - can't use any special characters
#  - do not use keywords

# Pyhton uses Dynamic Typing
# ie, you can reassign variables to different data types
my_dogs = 2

my_dogs = ["sammy","Frankie"]
# the above is not ok in C++

a = 5
# type() prints the datatype of the variable
print(type(a))
print(type(my_dogs))

my_income = 100
tax_rate = 0.1

my_taxes = my_income * tax_rate
print(my_taxes)
