def even_odd_filter(**kwargs):
    keys = kwargs.keys()
    result = {}
    if "even" in keys:
        even_list = kwargs["even"]
        even_list = [number for number in even_list if number % 2 == 0]
        result["even"] = even_list
    if "odd" in keys:
        odd_list = kwargs["odd"]
        odd_list = [number for number in odd_list if number % 2 != 0]
        result["odd"] = odd_list
    return result
