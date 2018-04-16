ioc_container = {}
'''IoC-container is simple dictionary with type as keys, and object as values
Notice, that type of value object can be not equal with key type. 
Key type is just a 'label' for object to resolving and injecting it. '''


def register(obj: object):
    """ Register object in IoC-container with it real type """
    obj_class = type(obj)
    ioc_container[obj_class] = obj


def register_as(obj: object, obj_class: type):
    """ Register object in IoC-container as object with desired type """
    if isinstance(obj, obj_class):
        ioc_container[obj_class] = obj


def resolve(obj_class: type):
    """ Return object with desired class from IoC-container """
    if obj_class in ioc_container:
        return ioc_container[obj_class]
    else:
        return None
