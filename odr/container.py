from odr.exceptions import NoRegisterObjectException

ioc_container = {}
''' IoC-container is simple dictionary with type as keys, and object as values.
Notice, that type of value object can be not equal with key. 
Object can be registered with base type or just with some type, not corresponding with this object. '''

ioc_container_labeled = {}


def register(obj: object):
    """ Register object in IoC-container with it real type """
    obj_class = type(obj)
    ioc_container[obj_class] = obj


def register_as(obj: object, obj_class: type):
    """ Register object in IoC-container as object with desired type """
    if isinstance(obj, obj_class):
        ioc_container[obj_class] = obj


def register_with_label(obj: object, label: str):
    ioc_container_labeled[label] = obj


def resolve(obj_class: type):
    """ Return object with desired class from IoC-container """
    if obj_class in ioc_container:
        return ioc_container[obj_class]
    else:
        raise NoRegisterObjectException
