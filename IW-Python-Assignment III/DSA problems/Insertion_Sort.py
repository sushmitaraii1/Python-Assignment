def InsertionSort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


arr = [64, 34, 25, 568, 12, 22, 11, 90]
print("List before sorting is: {}".format(arr))
result = InsertionSort(arr)
print("The ascending order of given list by bubble sort is: {}".format(result))