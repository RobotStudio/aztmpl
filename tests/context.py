"""Context module
Reference this from your tests to include the application.

Can be referenced like so:
```python
from .context import sample
```
"""
import os
import sys

#pylint: disable=wrong-import-position
sys.path.insert(0, os.path.abspath('..'))

#pylint: disable=unused-import
import az
