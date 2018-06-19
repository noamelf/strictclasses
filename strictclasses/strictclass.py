from functools import partial
from dataclasses import dataclass


def strict(cls):
    def _strict(self):
        for attr, _type in self.__annotations__.items():
            assert isinstance(getattr(self, attr), _type), f'{attr} is not an instance of {_type}'

    cls.strict = _strict
    return cls


def strict_dataclass(_cls=None, **kwargs):
    if _cls is None:
        return partial(strict_dataclass, **kwargs)
    cls = dataclass(_cls, **kwargs)
    strict_cls = type(cls.__name__, (_StrictData, cls), {})
    strict_cls.__module__ = cls.__module__
    return strict_cls


class _StrictData:
    def __setattr__(self, key, value):
        _type = self.__annotations__[key]
        assert isinstance(value, _type), f'{key} is not an instance of {_type}'
        super().__setattr__(key, value)
