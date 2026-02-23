def binary_search(arr, low, high, key):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)


arr = [2, 4, 6, 8, 10, 12]
key = 10

result = binary_search(arr, 0, len(arr)-1, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)

# Time complexity : O(log n)