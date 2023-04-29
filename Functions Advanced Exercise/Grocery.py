def grocery_store(**kwargs):
    keys_sorted = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for tuple in keys_sorted:
        result.append(f'{tuple[0]}: {tuple[1]}')
    return "\n".join(result)
