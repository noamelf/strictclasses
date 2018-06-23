import pytest

from strictclasses import strictclass


def test_strict():
    @strictclass
    class Foo:
        bar: int

    with pytest.raises(TypeError):
        Foo('3')

    foo = Foo(3)
    with pytest.raises(TypeError):
        foo.bar = '3'
