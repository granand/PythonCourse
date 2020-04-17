
#myfile = open('/Users/Anand/PycharmProjects/PythonCourse/myfile.txt')
myfile = open("myfile.txt")

# read() grabs everything as one  string
contents = myfile.read()
print(contents)
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
# returns everything  as a list
# returns ['This is the first line\n', 'This is the second line\n', 'This is the third line']
print(myfile.readlines())


myfile.close()

# This is the new style and doesn't need file close to be coded
with open("myfile.txt") as my_new_file:
    print(my_new_file.read())

# modes
# mode = 'r' - is read only which is also default
# mode = 'w' - is write only (overwrites or creates new file)
# mode = 'a' - is append only (will add on to files)
# mode = 'r+' - is reading and writing
# mode = 'w' - is writing and reading (Overwrites existing files or creates a new file)

with open("myfile.txt",mode="r") as f:
    print(f.read())

with open("myfile.txt",mode="a") as f:
    f.write("\nFourth line")

with open("myfile.txt", mode="r") as f:
    print(f.read())

with open("out.txt",mode="w") as f:
    f.write("\nThis is sample out line")

with open("out.txt",mode="r") as f:
    print(f.read())