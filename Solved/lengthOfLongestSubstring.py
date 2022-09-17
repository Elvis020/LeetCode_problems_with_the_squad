def lengthOfLongestSubstring(s):
    my_map = {}
    starting_point,max_length = 0,0
    for index,element in enumerate(s):
        if element in my_map and starting_point <= my_map[element]:
            starting_point = my_map[element]+1
        else:
            # Uses the difference btn the index of the current element and the starting_point
            max_length = index-starting_point+1 if index-starting_point+1>max_length else max_length
        my_map[element] = index
    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("dvdf"))
