def isHappy(n):
    is_happy = True
    j=0
    # print(n**2)
    while True:
        if len(str(n**2)) == 1 :
            return not is_happy
        for i in str(n):
            j += int(i) ** 2
            if len(str(j)) == 1:
                if j == 1:
                    return is_happy
                else:
                    return not is_happy




# print(isHappy(19))
# print(isHappy(2))
print(isHappy(4))
# print(isHappy(7))