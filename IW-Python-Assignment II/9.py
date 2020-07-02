# 9. Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return
# the index of the item if found. It should return -1 if the item is not found.

def binary_search(seq, item):
    for element in seq:
        if element == item:
            return seq.index(element)
            break
    else:
        return -1


lst = [1, 3, 5, 56, 7, 54, 756, 67]
result = binary_search(lst, 0)
print(result)
