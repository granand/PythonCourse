
try :
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Error in calculating square of the number in list")


x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print('cannot divide by zero')
finally:
    print("All Done")

print()

def ask():
    while True:
        try:
            num = int(input("Enter a Number :"))
            print("Square of the number {}".format(num**2))
            break
        except:
            print('Error Occurred Please try again ')

#ask()

# another way using else

def ask1():
    while True:
        try:
            num = int(input("Enter a Number :"))
        except:
            print('Error Occurred Please try again ')
#      continue is optional
            continue
        else:
            break

    print("Square of the number {}".format(num ** 2))

ask1()


