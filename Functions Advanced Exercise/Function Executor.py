def func_executor(*args):
    result_list = []
    for tuple in args:
        func = tuple[0]
        data = tuple[1]

        result = func(*data)
        result_list.append(f'{func.__name__} - {result}')
    return "\n".join(result_list)
