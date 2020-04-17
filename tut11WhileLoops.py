#
# break   : breaks out of the current closest  enclosing loop
# continue: Goes to the top of the current closest  enclosing loop
# pass    : Does nothing at all
#
x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("X is not less than 5")


x = [1,2,3]

for item in x:
    # comment
    pass

my_string = "samy"

# the below code skips the char a and prints the other letter in string
for letter in my_string:
    if letter == "a":
        continue
    print(letter)


# the below code prints s and then breaks the loop when the first a is encountered
for letter in my_string:
    if letter == "a":
        break
    print(letter)


# the below code prints 0 and 1 and then breaks the while loop when 2 is encountered
x = 0
while x < 5:
    if x == 2:
        break
    print(f"The current value of x is {x}")
    x += 1