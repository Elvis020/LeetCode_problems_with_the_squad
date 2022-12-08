# Method 1 not approved, used -
def test_add(a: int, b: int) -> int:
    return a - ~b - 1


# Using XOR and &, with left-shift <<
def test_add(a: int, b: int):
    # 0xffffffff is used to handle the negative case
    while (b&0xffffffff) != 0:
        tmp =(a & b) << 1
        a = a^b
        b = tmp
    return a&0xffffffff if b>0xffffffff else a
