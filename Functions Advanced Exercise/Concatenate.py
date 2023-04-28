def concatenate(*args, **kwargs):
    arguments = ""
    for arg in args:
        arguments += arg
    kwargs_keys = kwargs.keys()
    for key in kwargs_keys:
        if key in arguments:
            arguments = arguments.split(key)
            arguments = kwargs[key].join(arguments)
    return arguments
