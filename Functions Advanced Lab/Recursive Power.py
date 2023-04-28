def recursive_power(number, power, result=1):
    if power > 0:
        result *= number
        power -= 1
        return recursive_power(number, power, result)
    else:
        return result
