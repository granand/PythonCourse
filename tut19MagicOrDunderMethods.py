mylist = [1,2,3]

print(len(mylist))
print(mylist)

class Sample():
    pass

mysample = Sample()

# gives error - TypeError: object of type 'Sample' has no len()
#print(len(mysample))

# prints <__main__.Sample object at 0x1072b1890> that is is an object of Sample class
# doesn't print anything like when we printed the list
print(mysample)

# How to use the built in functions of python work for the user defined objects
# That is where the Magic or Dunder methods


class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"{self.title} by {self.author} is being deleted")

b = Book('Python Rocks','Anand',200)
print(b)
print(len(b))

# del is the built-in function that deletes the variables from computers memory
# the below will delete the object b from the memory
# If you want to perform special operations when delete occur you can define them in __del__ function
del b

# After deleting you cannot access b
# It will give NameError: name 'b' is not defined
# print(b)
