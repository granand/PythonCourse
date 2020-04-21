# An often confusing part of python is a mysterious line of code
#     if __name__ == "__main__"

# sometimes when you are importing from a module, you would like to know whether a modules function is
# being used as an import or if you are using the original.py of that module

# one.py

def func():
    print("func() in one.py")

print("Top Level in one.py")


if __name__ == "__main__":
    print("one.py is being run directly..")
else:
    print("one.py is being imported..")


#########

# the idea is all the definitions are in the script in the sequence
# And all the execution is below the condition
# if __name__ == "__main__":
#     RUN THE SCRIPT
#     All the script execution flow is given here
