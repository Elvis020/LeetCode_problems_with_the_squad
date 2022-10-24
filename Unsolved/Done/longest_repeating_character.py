

def characterReplacement(s:str,k:int):
    # This solution is implemented using the 2 pointer approach
    dict = {}
    result,max_count = 0,0
    left = 0 

    for right_index,right_element in enumerate(s):
        # Getting the count of letters from the right
        dict[right_element] = 1 + dict.get(right_element,0)

        # Comparing the count of letters in the dictionary to get the max value, 
        # this method is better than using the max() in-built function, 
        # which is O(n) of the dictionary values
        max_count = dict[right_element] if dict[right_element] > max_count else max_count

        if (right_index-left + 1) - max_count > k:
            # We start moving left pointer if the range is greater than k
            dict[s[left]] -= 1
            left += 1
        result = max(result,right_index-left+1)

    return result
