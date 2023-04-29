def age_assignment(*args, **kwargs):
    names = list(args)
    name_to_age_dict = {}
    for key, value in kwargs.items():
        for name in names:
            if key in name:
                name_to_age_dict[name] = value
    name_to_age_dict = sorted(name_to_age_dict.items(), key=lambda x: x[0])
    result = []
    for tuple in name_to_age_dict:
        result.append(f'{tuple[0]} is {tuple[1]} years old.')
    return "\n".join(result)
