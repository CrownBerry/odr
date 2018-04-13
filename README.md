# Óðr
## Desciprion
Odr (Óðr) is a very simple realisation of Dependency Injection pattern with global IoC-Container and simple decorator to inject object.
## Install
```
pip install odr
```
## Usage
If we need outer class, depends on inner class, just use `@inject` decorator:
```python
class InnerClass:
    def __init__(self):
        self.foo = 42

class OuterClass:
    @inject
    def __init__(self, inner: InnerClass):
        print(inner.foo)
        self.foo = inner.foo
```
##### Don't forget to annotate argument with desired class
But before create a instance of `OuterClass`, we need to register instance of InnerClass in our `IoC Container`:
```python
from odr.container import register

inner = InnerClass()
register(inner)
```
And now, when we create instance of `OuterClass` inner will be correctly inject into it:
```python
outer = OuterClass()
print(outer.foo)
>>> 42
```
However, if we want to get registered object from IoC-Container we can simple resolve it:
```python
from odr.container import resolve

inner = resolve(InnerClass)
print(inner.foo)
>>> 42
```
Enjoy!