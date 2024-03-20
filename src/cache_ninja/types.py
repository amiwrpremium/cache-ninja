"""
# Types

This module contains type aliases and type variables used throughout the package.

Type variables:
    - Serializable: A type variable that can be serialized.

Type aliases:
    - DictStrSerializable: A dictionary with string keys and any values.
"""

from typing import TypeVar

# Type variables
Serializable = TypeVar(
    'Serializable',
    str, bytes, dict, int, float, object, list, tuple, set, frozenset, bool, bytearray, memoryview
)

# Type aliases
DictStrSerializable = dict[str, Serializable]
