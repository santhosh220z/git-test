def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(arr)
    target = int(input("select a number to search from the array:"))

    result = binary_search(arr, target)
    if result != -1:
        print("Element found at index:",result)
    else:
        print("Element not found in the array.")
