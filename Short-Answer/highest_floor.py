def find_floor(floor):
    low = 0
    high = len(floor) - 1
    while low < high:
        middle = (low + high) // 2
        if floor[middle] == 1:
            if floor[middle-1] == 0:
                return middle
            else:
                high = middle - 1
        elif floor[middle] == 0:
            if floor[middle+1] == 1:
                return middle + 1
            else:
                low = middle + 1


print(find_floor([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))


def binary_search(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l)/2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it is in the left subarray
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)

        # Else the element is in the right subarray
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1
