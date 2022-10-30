# Searshing

# ===> Linear Search
# worst case ---> O(n) = first element
# best case  ---> O(1) = last element
def linearSearch(arr, target):
    i = 0
    n = len(arr)
    while i <= n:
        if arr[i] == target:
            return i
        i += 1
    return -1


print(linearSearch([1, 2, 5, 6, 8, 9], 9))


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
