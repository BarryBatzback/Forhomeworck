
def get_multiplied_digits(number):

    str_number = str(number)

    first = int(str_number[0])

    if len(str_number) > 1:
        prod = get_multiplied_digits(int(str_number[1:]))
        if prod == 0:
            return first
        return first * prod
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)
