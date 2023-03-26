import itertools
from collections import Counter


# Timeout
# def checkInclusion(s1: str, s2: str) -> bool:
#     i, j = 0, len(s1)
#     while j <= len(s2):
#         if s2[i:j] in list(map(lambda x: ''.join(x), itertools.permutations(s1))):
#             return True
#         i += 1
#         j += 1
#     return False

# Works(22...%)
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1_count = Counter(s1)
    i, j = 0, len(s1)
    while j <= len(s2):
        if Counter(s2[i:j]) == s1_count:
            return True
        i += 1
        j += 1
    return False


print(checkInclusion("ab", "eidbao"))
print(checkInclusion("ab", "eidboaoo"))
# print(checkInclusion("adc", "dcda"))
