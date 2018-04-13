# Óðr
## Install
```
Work in progress
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
##### Don't forget to decorate argument with desired class
But before create a instance of `OuterClass`, we need to register instance of InnerClass in our `IoC Container`:
```python
from odr.container import register_as

inner = InnerClass()
register_as(inner, InnerClass)
```
And now, when we create instance of `OuterClass` inner will be correctly inject into it:
```python
outer = OuterClass()
print(outer.foo)
>>> 42
```
Enjoy!