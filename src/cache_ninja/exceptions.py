"""
# Core Exceptions

This module contains the set of CacheNinja's exceptions.

## Exception Hierarchy

- CacheNinjaException
    - SerializationError
    - CacherError
    - InvalidChoiceError

## Example

Here's an example of how to use a CacheNinjaException:
```python
    from cache_ninja.exceptions import SerializationError

    try:
        # code
    except SerializationError as e:
        # handle exception
```
"""


class CacheNinjaException(Exception):
    """Base class for all exceptions"""


class SerializationError(CacheNinjaException):
    """Error in serialization"""


class CacherError(CacheNinjaException):
    """Error in cacher"""


class InvalidChoiceError(CacheNinjaException):
    """Error in choice"""
