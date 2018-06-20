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
f.strict() # -> TypeError: bar is not an instance of <class 'int'>
```


```python
from strictclasses import strictclass

@strictclass
class Foo:
    bar: int


f = Foo('3') # -> TypeError: bar is not an instance of <class 'int'>
f = Foo(3)
f.bar = 3.3 # -> TypeError: bar is not an instance of <class 'int'>
```
