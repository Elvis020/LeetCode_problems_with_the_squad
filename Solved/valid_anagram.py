def isAnagram(s: str, t: str) -> bool:
    return False if len(s) != len(t) else sorted(s) == sorted(t)