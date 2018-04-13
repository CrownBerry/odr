from odr.container import register_as
from odr.injector import inject


class InnerClass:
    def __init__(self):
        self.foo = 42


class OuterClass:
    @inject
    def __init__(self, inner: InnerClass):
        print(inner.foo)
        self.foo = inner.foo


class TestMain:
    def test_something(self):
        a = InnerClass()
        register_as(a, InnerClass)
        b = OuterClass()
        assert b.foo == 42
