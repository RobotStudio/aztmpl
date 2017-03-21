"""Examples loaded from pytest documentation
Any files named *_test.py or test_*.py recursively found will be executed

Access your app like this:
```python
from .context import aztmpl
```
"""

import pytest

def func(arg_x):
    """Returns the value passed +1"""
    return arg_x + 1

def test_answer():
    """Asserts that the result of func(3) == 4"""
    assert func(3) == 4

def raise_exit():
    """Raises SystemExit(1)"""
    raise SystemExit(1)

def test_mytest():
    """Asserts that raise_exit raises exit"""
    with pytest.raises(SystemExit):
        raise_exit()

class TestClass:
    """This is a test class"""
    valx = None
    valy = None

    def test_one(self):
        """Asserts that "this" has an "h" in it"""
        self.valx = "this"
        assert 'h' in self.valx

    def test_two(self):
        """Asserts that an instance of the function t1000 has the attribute __name__"""
        def t1000():
            """PASS"""
            pass
        self.valy = t1000
        assert hasattr(self.valy, '__name__')
        assert self.valy.__name__ == "t1000"

def test_needsfiles(tmpdir):
    """Validates that a tmpdir can get created"""
    print(tmpdir)
    assert True
