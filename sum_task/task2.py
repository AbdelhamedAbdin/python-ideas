import re


def summation(string_of_number):
    user_input = input(string_of_number)
    seek = re.findall(r'[-+]?\d*\.\d+|\d+', user_input)
    sum = 0.0

    for s in seek:
        number = float(s)
        sum += float(number)
    return float(sum)


print(summation("string of integers: "))
