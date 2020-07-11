# Taking last elemtent as pivot


def partition(arr, low, high):
    i = (low - 1)

    pivot = arr[high]

    for j in range(low, high):

        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def QuickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)


arr = [9, -3, 5, 2, 6, 8, -6, 1, 3]
n = len(arr)
QuickSort(arr, 0, n - 1)
print("Sorted array is:", arr)
