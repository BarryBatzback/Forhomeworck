def NUMBERS(n):
    result = ""
    pairs = []

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))

    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            result += f"{pair[0]}{pair[1]}"

    return result

print(NUMBERS(3))
print(NUMBERS(4))
print(NUMBERS(5))
print(NUMBERS(6))
print(NUMBERS(7))
print(NUMBERS(8))
print(NUMBERS(9))
print(NUMBERS(10))
print(NUMBERS(11))
print(NUMBERS(12))
print(NUMBERS(13))
print(NUMBERS(14))
print(NUMBERS(15))
print(NUMBERS(16))
print(NUMBERS(17))
print(NUMBERS(18))
print(NUMBERS(19))
print(NUMBERS(20))