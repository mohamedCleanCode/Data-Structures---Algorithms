# Searshing

# ===> Linear Search
# worst case ---> O(n) = first element
# best case  ---> O(1) = last element
from genericpath import samestat


def linearSearch(arr, target):
    i = 0
    n = len(arr)
    while i <= n:
        if arr[i] == target:
            return i
        i += 1
    return -1


print(linearSearch([1, 2, 5, 6, 8, 9], 9))

print("#" * 30)
# ===> Binary Search
# worst case ---> O(lg(n)) = first element | last element
# best case  ---> O(1)     = middle element


def binarySearch(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binarySearch([1, 3, 5, 7, 9], 3))


# Sorting

print("#" * 30)
# Bubbl Sort

print("#" * 30)
# Selection sort

arr = [3, 8, 5, 2]


def findSamllest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def slectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSamllest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(slectionSort([3, 8, 5, 2]))
