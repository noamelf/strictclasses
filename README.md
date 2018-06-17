# strictclasses

This is a validation companion to `dataclasses`. It adds a validation strict
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
