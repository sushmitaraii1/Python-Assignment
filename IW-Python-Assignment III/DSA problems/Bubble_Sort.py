def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


arr = [64, 34, 25, 568, 12, 22, 11, 90]
print("List before sorting is: {}".format(arr))
result = BubbleSort(arr)
print("The ascending order of given list by bubble sort is: {}".format(result))