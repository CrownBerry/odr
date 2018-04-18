ioc_container = {}
''' IoC-container is simple dictionary with type as keys, and object as values.
Notice, that type of value object can be not equal with key. 
Object can be registered with base type or just with some type, not corresponding with this object. '''

ioc_container_labeled = {}
''' Labeled IoC-container is simple dictionary with string as keys, and object as values.
Object can be registered with label, that corresponding kwarg name in the implemented function. '''


