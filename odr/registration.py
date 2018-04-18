from odr.container import ioc_container, ioc_container_labeled
from odr.exceptions import NoRegisterObjectException


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