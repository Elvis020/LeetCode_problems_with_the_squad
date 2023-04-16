def contains_duplicate(nums):
    """Checks if the length of a set of nums is the same as the length of the nums """
    return len(set(nums)) != len(nums)