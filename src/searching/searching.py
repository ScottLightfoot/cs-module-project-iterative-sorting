def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    lower_bound = 0
    upper_bound = len(arr)
    mid = int(upper_bound/2)

    while upper_bound - lower_bound > 0:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            upper_bound = mid
            mid = int(upper_bound/2)
        else:
            lower_bound = mid
            mid += int((upper_bound - lower_bound)/2)

    else:
        return -1
