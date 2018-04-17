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