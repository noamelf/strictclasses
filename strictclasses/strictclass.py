from functools import partial
from dataclasses import dataclass


def strictclass(_cls=None, **kwargs):
    """
    wrapper on dataclasses dataclass decorator that add type checking
    """
    if _cls is None:
        return partial(strictclass, **kwargs)
    cls = dataclass(_cls, **kwargs)
    strict_cls = type(cls.__name__, (_StrictData, cls), {})
    strict_cls.__module__ = cls.__module__
    return strict_cls


class _StrictData:
    def __setattr__(self, key, value):
        self.validator(key, value, annotation=self.__annotations__[key])
        super().__setattr__(key, value)

    @staticmethod
    def validator(name, value, annotation):
        # todo: support more complex type annotations in the feature
        # todo: For Example: typing.Dict[str,List[float]]
        if not isinstance(value, annotation):
            raise TypeError(f'{name} is not an instance of {annotation}')
