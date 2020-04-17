# Lists are ordered sequences
# can hold variety of objects
# supports indexing and slicing
# unlike String we can mutate lists
# Lists are Mutable

my_list = [1,2,3]

my_list1 = ["STRING",100,23.7]

# returns the length of the list
print(len(my_list))
print(len(my_list1))

my_num_list = ["one","two","three"]

# returns one
print(my_num_list[0])

# returns ['two', 'three']  starts at index position 1 and until end
print(my_num_list[1:])

my_num_list1 = ["four","five"]

# concatenates the list
new_list = my_num_list + my_num_list1

# returns ['one', 'two', 'three', 'four', 'five']
print(new_list)

# unlike String we can mutate lists
new_list[0] = "ONE ALL CAPS"

# prints ['ONE ALL CAPS', 'two', 'three', 'four', 'five']
print(new_list)

# Adding an elment at the end of the list
new_list.append("SIX")
print(new_list)

# removing an element from the list
# pop removes from the end of the list
new_list.pop()
# returns the list ['ONE ALL CAPS', 'two', 'three', 'four', 'five']
print(new_list)

# popped element can be stored in a variable
# returns five
popped_item = new_list.pop()
print(popped_item)

# passing an index to the pop will remove the element in that position
# returns ONE ALL CAPS
popped_item = new_list.pop(0)
print(popped_item)

# default for the pop is pop(-1) and this why it pops from the end
# pop(-1) will also pop from the end
popped_item = new_list.pop(1)
# returns three
print(popped_item)

new_list = ['e','a','c','d','b']
num_list = [4,1,8,3]

# returns None
print(new_list.sort())
# the reason for that is sort does the sorting inplace
# it doesn't return anything
# if you print the type of the returned item, it is a NoneType
# prints <class 'NoneType'>
print(type(new_list.sort()))

# prints ['a', 'b', 'c', 'd', 'e']
print(new_list)


num_list.sort()
# returns [1, 3, 4, 8]
print(num_list)

# reverse sort using the reverse()
num_list.reverse()
# returns [8, 4, 3, 1]
print(num_list)
