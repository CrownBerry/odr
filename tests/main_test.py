import pytest

from odr.container import register, register_as, resolve
from odr.exceptions import NoRegisterObjectException
from odr.injector import inject


class InnerClass:
    def __init__(self, foo=42):
        self.foo = foo


class AnotherInnerClass(InnerClass):
    def __init__(self, foo=42):
        super().__init__()


class OuterClass:
    @inject
    def __init__(self, inner: InnerClass):
        print(inner.foo)
        self.foo = inner.foo


class AnotherOuterClass:
    @inject
    def __init__(self, inner: InnerClass):
        print(inner.foo)
        self.foo = inner.foo


class ExceptionalClass:
    @inject
    def __init__(self, outer: OuterClass):
        print("Hello darkness my old friend")
        self.foo = outer.foo


class TestPositiveInjection:
    def test_register(self):
        a = InnerClass()
        register(a)
        b = OuterClass()
        assert b.foo == 42

    def test_register_as(self):
        a = AnotherInnerClass()
        register_as(a, InnerClass)
        b = OuterClass()
        assert b.foo == 42

    def test_resolve(self):
        a = resolve(InnerClass)
        assert a.foo == 42
        b = AnotherOuterClass(a)
        assert b.foo == 42


class TestManualPassing:
    def test_pass_arg(self):
        a = InnerClass(32)
        b = OuterClass(a)
        assert b.foo == 32

    def test_pass_kwarg(self):
        a = InnerClass(24)
        b = OuterClass(inner=a)
        assert b.foo == 24


class TestExceptions:
    def test_raise_exception_on_inject(self):
        with pytest.raises(NoRegisterObjectException):
            b = ExceptionalClass()

    def test_raise_exception_on_resolve(self):
        with pytest.raises(NoRegisterObjectException):
            c = resolve(str)
