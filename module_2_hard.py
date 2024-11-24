def generate_password(n):
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

print(generate_password(3))
print(generate_password(4))
print(generate_password(5))
print(generate_password(6))
print(generate_password(7))
print(generate_password(8))
print(generate_password(9))
print(generate_password(10))
print(generate_password(11))
print(generate_password(12))
print(generate_password(13))
print(generate_password(14))
print(generate_password(15))
print(generate_password(16))
print(generate_password(17))
print(generate_password(18))
print(generate_password(19))
print(generate_password(20))