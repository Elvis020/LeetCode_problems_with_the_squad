def count_bits(n):
    return list(map(lambda x: bin(x)[2:].count('1'), range(n + 1)))


# TODO: Write unit tests
print(count_bits(2))
print(count_bits(5))
