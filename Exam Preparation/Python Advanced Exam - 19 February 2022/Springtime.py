def start_spring(**qwargs):
    func_dict = {}
    for key in qwargs:
        value = qwargs[key]
        if value not in func_dict.keys():
            func_dict[value] = [key]
        else:
            func_dict[value].append(key)
    func_dict = sorted(func_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    return_list = []
    for key in func_dict:
        return_list.append(f'{key[0]}:')
        lst = sorted(key[1], key=lambda x: x)
        for el in lst:
            return_list.append(f'-{el}')
    return "\n".join(return_list)
