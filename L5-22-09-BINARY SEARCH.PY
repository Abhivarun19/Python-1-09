#implementing binary search
def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)
element = 39
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 32, 36, 40]

print("Searching for {}".format(element))
print("Index of {}: {}".format(element, binary_search(array, element, 0, len(array))))
