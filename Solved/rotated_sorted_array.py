def bs(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1

    return -1


def bs_2(arr, target):
    try:
        return arr.index(target)
    except:
        return -1


# TODO: Write unit test
print(bs([-1, 0, 3, 5, 9, 12], 9))
print(bs_2([-1, 0, 3, 5, 9, 12], 9))
