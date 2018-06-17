# strictclasses

**Disclaimer: this is beta software, API is not stable.**

This is a validation companion to `dataclasses`. 

It adds the `strict` method to the dataclass to validate the types are correct.
Usage:

```python
from dataclasses import dataclass
from strictclasses import strict

@strict
@dataclass
class Foo:
    bar: int


f = Foo('3')
f.strict() # -> AssertionError: bar is not an instance of <class 'int'>
```
