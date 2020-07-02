# 11. Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations,
# find the extension. For README.txt, the extension should be txt. Write code using slice operations that will give
# the name without the extension. Does your code work on filenames of arbitrary length?


# returning filename without extension
def files(name):
    dot = name.index('.')
    return name[:dot], name[dot + 1:]


example1 = 'README.md'
example2 = "Read.txt"

file_name1, estension1 = files(example1)
print("The filename is {} and extension is {}".format(file_name1, estension1))

file_name2, estension2 = files(example2)
print("The filename is {} and extension is {}".format(file_name2, estension2))

# Yes my code works on filename with arbitrary length
