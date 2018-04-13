ioc_container = {}


def register_as(obj: object, obj_class: type):
    if isinstance(obj, obj_class):
        ioc_container[obj_class] = obj
