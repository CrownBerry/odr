from odr.container import ioc_container


def inject(f):
    def wrapper(*args, **kwargs):
        founded = {}
        print(kwargs)
        for name, arg_type in f.__annotations__.items():
            if type(arg_type) is type:
                if arg_type in ioc_container:
                    already_existed_args = [arg for arg in args if isinstance(arg, arg_type)]
                    if not already_existed_args:
                        founded[name] = ioc_container[arg_type]
            else:
                print("{0} annotation `{1}` is not a type".format(name, arg_type))
        return f(*args, **founded, **kwargs)

    return wrapper
