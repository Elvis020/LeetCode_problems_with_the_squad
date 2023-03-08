def longestConsecutive(nums):
    # Check if array is not empty
    if not nums: return 0

    # Initialize array
    arr = [min(nums)]
    bigger_arr = []

    # Sort the array
    nums.sort()

    # Loop through the array and compare the elements next to each other
    for index, element in enumerate(nums):

        # Check if the element is not the first one and subtract
        # current_element-prev_element to check if they are consecutive
        if index != 0 and element - nums[index - 1] == 1:
            arr.append(element)
        elif element - nums[index - 1] > 1:
            bigger_arr.append(arr) # If the next element is not consecutive, put it in a bigger arr
            arr = [element] # Start with the element that broke the comparison chain
    bigger_arr.append(arr)

    # Sort the arrays by len and pick the longest
    return len(sorted(bigger_arr, key=len)[-1])