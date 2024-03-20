""" # Abstract Serializer

This module defines the abstract class for serializer.

## Path: serializers/abstract.py

## Classes:
    Abstract: Abstract class for serializer.

## Dependencies:
    - abc:
        - ABC: Abstract Base Class.
        - abstractmethod: Decorator for abstract methods.
    - types:
        - Serializable: Type hint for serializable data.
"""

from abc import ABC, abstractmethod
from ..types import Serializable


class Abstract(ABC):
    """Abstract class for serializer.

    This class defines the abstract methods for serializer.

    Methods:
        serialize: Serialize data.
        deserialize: Deserialize data.
    """

    @abstractmethod
    def serialize(self, value: Serializable) -> str:
        """Serialize data.

        Args:
            value (Serializable): The data to serialize.

        Returns:
            str: The serialized data.
        """

        raise NotImplementedError

    @abstractmethod
    def deserialize(self, value: str) -> Serializable:
        """Deserialize data.

        Args:
            value (str): The data to deserialize.

        Returns:
            Serializable: The deserialized data.
        """

        raise NotImplementedError
