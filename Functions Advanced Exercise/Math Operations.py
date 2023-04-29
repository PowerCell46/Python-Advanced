def math_operations(*args, **kwargs):
    index = 1
    for number in args:
        if index == 1:
            kwargs["a"] += number
            index += 1

        elif index == 2:
            kwargs["s"] -= number
            index += 1

        elif index == 3:
            if number != 0:
                kwargs["d"] /= number
            index += 1

        elif index == 4:
            kwargs["m"] *= number
            index = 1
    elements = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for tuple in elements:
        result.append(f'{tuple[0]}: {tuple[1]:.1f}')
    return "\n".join(result)
