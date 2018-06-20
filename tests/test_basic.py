import pytest
from dataclasses import dataclass

from strictclasses import strict


def test_strict():
    @strict
    @dataclass
    class Foo:
        bar: int

    f = Foo('3')
    with pytest.raises(TypeError):
        f.strict()  # -> TypeError: bar is not an instance of <class 'int'>
