# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

lst = ['Sushmita', 'salina', 'shreya', 'upasana', 'John', 'ojaswee']

for name in lst:
    if name == 'John':
        print("You have friend named {}.".format(name))
        break
else:
    print("not found")

