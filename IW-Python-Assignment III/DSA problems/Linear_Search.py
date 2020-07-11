def search(lst, x):
    for i in range(len(lst)):

        if lst[i] == x:
            return i

    return -1


lst = [-6, -3, 1, 2, 3, 5, 6, 8, 9]
result = search(lst,9)
if result is not -1:
    print("Element found on index {}".format(result))
else:
    print("Elements not found")
