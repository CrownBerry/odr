from odr.container import ioc_container, ioc_container_labeled
from odr.exceptions import NoRegisterObjectException


def inject(f):
    """ Inject is decorator that check annotated args and kwargs of function and trying to find object
    with desired class in IoC-container. If object found, it passes into decorated function.
    Else, NoRegisterObject exception will be raise. """

    def wrapper(*args, **kwargs):
        founded = {}
        for name, arg_type in f.__annotations__.items():
            if type(arg_type) is type:
                already_existed_args = [arg for arg in args if isinstance(arg, arg_type)]
                if name in kwargs or len(already_existed_args) > 0:
                    continue
                if name in ioc_container_labeled:
                    founded[name] = ioc_container_labeled[name]
                elif arg_type in ioc_container:
                    founded[name] = ioc_container[arg_type]
                else:
                    raise NoRegisterObjectException
            else:
                print("{0} annotation `{1}` is not a type".format(name, arg_type))
        return f(*args, **founded, **kwargs)

    return wrapper
