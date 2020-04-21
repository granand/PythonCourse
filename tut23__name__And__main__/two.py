# two.py

import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    "two.py is being run directly "
else:
    "two.py is being imported"