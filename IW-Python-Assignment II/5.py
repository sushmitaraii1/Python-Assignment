# 5. Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it.
# Make more tuples with the corresponding information from your friends and append them to the list. Sort the list.
# When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name,
# last name, or age.

lst = []
tup1 = ('sushmita','rai',21)
lst.append(tup1)
tup2 = ('asshmita','pradhan',25)
lst.append(tup2)
tup3 = ('salina','thapa',27)
lst.append(tup3)
tup4 = ('sitosma','bahadur',31)
lst.append(tup4)

print("Original list is {}".format(lst))

lst.sort(key = lambda x: x[2])
print("List sorted wih third element is {}".format(lst))
