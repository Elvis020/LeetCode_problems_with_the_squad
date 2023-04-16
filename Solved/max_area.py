def maxArea(height):
    current_max = 0
    left, right = 0, len(height) - 1
    while left != right:
        area = min(height[left], height[right]) * (right - left)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        current_max = area if area > current_max else current_max
    return current_max

# TODO: Write unit tests
