from math import log


def calculate_log(number, base):
    if base == "natural":
        print(f'{log(number):.2f}')
    else:
        print(f'{log(number, int(base)):.2f}')


number = int(input())
base = input()
calculate_log(number, base)
