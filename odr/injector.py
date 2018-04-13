from odr.container import ioc_container


def inject(f):
    def wrapper(*args, **kwargs):
        founded = {}
        for name, arg_type in f.__annotations__.items():
            if type(arg_type) is type:
                if arg_type in ioc_container:
                    founded[name] = ioc_container[arg_type]
                print("\n{0} of type {1}".format(name, arg_type))
            else:
                print("\n{0} has annotate {1}".format(name, arg_type))
        return f(*args, **founded, **kwargs)

    return wrapper
