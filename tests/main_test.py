from odr.container import register, register_as, resolve
from odr.injector import inject


class InnerClass:
    def __init__(self):
        self.foo = 42


class AnotherInnerClass(InnerClass):
    def __init__(self):
        super().__init__()


class OuterClass:
    @inject
    def __init__(self, inner: InnerClass):
        print(inner.foo)
        self.foo = inner.foo


class AnotherOuterClass:
    def __init__(self, inner: InnerClass):
        print(inner.foo)
        self.foo = inner.foo


class TestMain:
    def test_autoregister(self):
        a = InnerClass()
        register(a)
        b = OuterClass()
        assert b.foo == 42

    def test_register_with_classname(self):
        a = AnotherInnerClass()
        register_as(a, InnerClass)
        b = OuterClass()
        assert b.foo == 42

    def test_manual_pass(self):
        a = resolve(InnerClass)
        b = AnotherOuterClass(a)
        assert b.foo == 42
