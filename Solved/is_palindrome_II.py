# Works but there is a time limit
# def validPalindrome(s: str) -> bool:
#     for index, _ in enumerate(list(s)):
#         word = list(s)[:index] + list(s)[index + 1:]
#         if ''.join(word) == ''.join(word[::-1]):
#             return True
#     return False


def validPalindrome_II(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s, left, right - 1) | is_palindrome(s, left + 1, right)
        left += 1
        right -= 1
    return True


def is_palindrome(s, left, right):
    #  Need to use the 2-pointer for this solution to work
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(validPalindrome_II('cbbcc'))  # True
print(validPalindrome_II('abca')) # True
print(validPalindrome_II('abc')) # False
print(validPalindrome_II('pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip')) # False
print(validPalindrome_II('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga')) # True

# cbbcc


# print(validPalindrome_II('cbbcc'))  # True
# print(validPalindrome('abca')) # True
# print(validPalindrome('abc')) # False
# print(validPalindrome('pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip')) # False
# print(validPalindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga')) # True
