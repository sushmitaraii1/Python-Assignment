# 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the
# list. What is the first item on the list? What is the second item on the list?

lst = []
print(id(lst))
lst.append("wandana")
lst.append('Hari')
lst.append("shyam")
lst.append("sita")
print(id(lst))

print(lst)

lst.sort()
print(lst)
print("  The first element on list is {} \n  The second element is {}.".format(lst[0],lst[1]))