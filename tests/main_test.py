import pytest

from odr.registration import register, register_as, register_with_label, resolve
from odr.exceptions import NoRegisterObjectException
from tests.mocks import InnerClass, AnotherInnerClass, OuterClass, AnotherOuterClass, ExceptionalClass


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

    def test_label_priority(self):
        a = InnerClass(20)
        b = InnerClass(30)
        register_with_label(b, "inner")
        register(a)
        c = OuterClass()
        assert c.foo == 30


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
