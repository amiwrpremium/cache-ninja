"""# Abstract Cacher.

This module contains the abstract class for cacher.

## Path: backends/abstract.py

## Classes:
    - Abstract: Abstract class for cacher.

## Dependencies:
    - abc:
        - ABC: Abstract Base Class.
        - abstractmethod: Decorator for abstract methods.
    - serializers:
        - Abstract: Abstract class for serializers.
    - types:
        - DictStrSerializable: Serializable dictionary.
        - Serializable: Serializable type.
"""

from abc import ABC, abstractmethod
from ..serializers import Abstract as AbstractSerializer
from ..types import DictStrSerializable, Serializable


class Abstract(ABC):
    """Abstract class for cacher.

    This class defines the abstract methods for cacher.

    Methods:
        - set: Save the key-value data.
        - get: Get the data.
        - delete: Delete data.
        - exists: Check if data exists.
        - expire: Set the expiration time of a key.
        - ttl: Get the expiration time of a key.
        - keys: Get the keys that match the pattern.
        - incr: Increment the value of a key.
        - decr: Decrement the value of a key.
        - flush: Delete all keys.
        - batch_set: Save multiple key-value data.
        - batch_get: Get multiple data.
        - batch_delete: Delete multiple data.
        - batch_exists: Check if multiple data exists.
        - batch_ttl: Get the expiration time of multiple keys.
        - batch_incr: Increment the value of multiple keys.
        - batch_decr: Decrement the value of multiple keys.
        - a_set: Save the key-value data (async).
        - a_get: Get the data (async).
        - a_delete: Delete data (async).
        - a_exists: Check if data exists (async).
        - a_expire: Set the expiration time of a key (async).
        - a_ttl: Get the expiration time of a key (async).
        - a_keys: Get the keys that match the pattern (async).
        - a_incr: Increment the value of a key (async).
        - a_decr: Decrement the value of a key (async).
        - a_flush: Delete all keys (async).
        - a_batch_set: Save multiple key-value data (async).
        - a_batch_get: Get multiple data (async).
        - a_batch_delete: Delete multiple data (async).
        - a_batch_exists: Check if multiple data exists (async).
        - a_batch_ttl: Get the expiration time of multiple keys (async).
        - a_batch_incr: Increment the value of multiple keys (async).
        - a_batch_decr: Decrement the value of multiple keys (async).

    Attributes:
        - serializer: The serializer to use.
    """

    serializer: AbstractSerializer

    def __init__(self, serializer: AbstractSerializer) -> None:
        """
        Initialize the cacher.

        Args:
            serializer (AbstractSerializer): The serializer to use.

        Returns:
            None
        """
        self.serializer = serializer

    @abstractmethod
    def set(self, key: str, value: Serializable, expire: int = 0, **kwargs) -> bool:
        """
        Save the key-value data.

        Args:
            key (str): The key to save the data.
            value (Any): The data to save.
            expire (int): The time to
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was saved, False otherwise.
        """

    @abstractmethod
    def get(self, key: str, **kwargs) -> Serializable:
        """
        Get the data.

        Args:
            key (str): The key to load the data.
            **kwargs: Additional arguments.

        Returns:
            Data loaded.
        """

    @abstractmethod
    def delete(self, key: str, **kwargs) -> bool:
        """Delete data.

        Args:
            key (str): The key to delete the data.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was deleted, False otherwise.
        """

    @abstractmethod
    def exists(self, key: str, **kwargs) -> bool:
        """Check if data exists.

        Args:
            key (str): The key to check if the data exists.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data exists, False otherwise.
        """

    @abstractmethod
    def expire(self, key: str, time: int, **kwargs) -> bool:
        """Set the expiration time of a key.

        Args:
            key (str): The key to set the expiration time.
            time (int): The time to set the expiration.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the expiration time was set, False otherwise.
        """

    @abstractmethod
    def ttl(self, key: str, **kwargs) -> int:
        """Get the expiration time of a key.

        Args:
            key (str): The key to get the expiration time.
            **kwargs: Additional arguments.

        Returns:
            int: The expiration time of the key.
        """

    @abstractmethod
    def keys(self, pattern: str, **kwargs) -> list:
        """Get the keys that match the pattern.

        Args:
            pattern (str): The pattern to match the keys.
            **kwargs: Additional arguments.

        Returns:
            list: The keys that match the pattern.
        """

    @abstractmethod
    def incr(self, key: str, delta: int = 1, **kwargs) -> int:
        """Increment the value of a key.

        Args:
            key (str): The key to increment the value.
            delta (int): The value to increment.
            **kwargs: Additional arguments.

        Returns:
            int: The value after the increment.
        """

    @abstractmethod
    def decr(self, key: str, delta: int = 1, **kwargs) -> int:
        """Decrement the value of a key.

        Args:
            key (str): The key to decrement the value.
            delta (int): The value to decrement.
            **kwargs: Additional arguments.

        Returns:
            int: The value after the decrement.
        """

    @abstractmethod
    def flush(self, **kwargs) -> bool:
        """Delete all keys.

        Args:
            **kwargs: Additional arguments.

        Returns:
            bool: True if all keys were deleted, False otherwise.
        """

    @abstractmethod
    def batch_set(self, data: DictStrSerializable, expire: int = 0, **kwargs) -> bool:
        """Save multiple key-value data.

        Args:
            data (DictStrSerializable): The data to save.
            expire (int): The time to
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was saved, False otherwise.
        """

    @abstractmethod
    def batch_get(self, keys: list[str], **kwargs) -> DictStrSerializable:
        """Get multiple data.

        Args:
            keys (list): The keys to load the data.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: Data loaded.
        """

    @abstractmethod
    def batch_delete(self, keys: list[str], **kwargs) -> bool:
        """Delete multiple data.

        Args:
            keys (list): The keys to delete the data.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was deleted, False otherwise.
        """

    @abstractmethod
    def batch_exists(self, keys: list[str], **kwargs) -> DictStrSerializable:
        """Check if multiple data exists.

        Args:
            keys (list): The keys to check if the data exists.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: True if the data exists, False otherwise.
        """

    @abstractmethod
    def batch_ttl(self, keys: list[str], **kwargs) -> DictStrSerializable:
        """Get the expiration time of multiple keys.

        Args:
            keys (list): The keys to get the expiration time.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: The expiration time of the keys.
        """

    @abstractmethod
    def batch_incr(self, keys: list[str], delta: int = 1, **kwargs) -> DictStrSerializable:
        """Increment the value of multiple keys.

        Args:
            keys (list): The keys to increment the value.
            delta (int): The value to increment.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: The value after the increment.
        """

    @abstractmethod
    def batch_decr(self, keys: list[str], delta: int = 1, **kwargs) -> DictStrSerializable:
        """Decrement the value of multiple keys.

        Args:
            keys (list): The keys to decrement the value.
            delta (int): The value to decrement.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: The value after the decrement.
        """

    @abstractmethod
    async def a_set(self, key: str, value: Serializable, expire: int = 0, **kwargs) -> bool:
        """
        Save the key-value data.

        Args:
            key (str): The key to save the data.
            value (Any): The data to save.
            expire (int): The time to
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was saved, False otherwise.
        """

    @abstractmethod
    async def a_get(self, key: str, **kwargs) -> Serializable:
        """
        Get the data.

        Args:
            key (str): The key to load the data.
            **kwargs: Additional arguments.

        Returns:
            Data loaded.
        """

    @abstractmethod
    async def a_delete(self, key: str, **kwargs) -> bool:
        """Delete data.

        Args:
            key (str): The key to delete the data.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was deleted, False otherwise.
        """

    @abstractmethod
    async def a_exists(self, key: str, **kwargs) -> bool:
        """Check if data exists.

        Args:
            key (str): The key to check if the data exists.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data exists, False otherwise.
        """

    @abstractmethod
    async def a_expire(self, key: str, time: int, **kwargs) -> bool:
        """Set the expiration time of a key.

        Args:
            key (str): The key to set the expiration time.
            time (int): The time to set the expiration.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the expiration time was set, False otherwise.
        """

    @abstractmethod
    async def a_ttl(self, key: str, **kwargs) -> int:
        """Get the expiration time of a key.

        Args:
            key (str): The key to get the expiration time.
            **kwargs: Additional arguments.

        Returns:
            int: The expiration time of the key.
        """

    @abstractmethod
    async def a_keys(self, pattern: str, **kwargs) -> list:
        """Get the keys that match the pattern.

        Args:
            pattern (str): The pattern to match the keys.
            **kwargs: Additional arguments.

        Returns:
            list: The keys that match the pattern.
        """

    @abstractmethod
    async def a_incr(self, key: str, delta: int = 1, **kwargs) -> int:
        """Increment the value of a key.

        Args:
            key (str): The key to increment the value.
            delta (int): The value to increment.
            **kwargs: Additional arguments.

        Returns:
            int: The value after the increment.
        """

    @abstractmethod
    async def a_decr(self, key: str, delta: int = 1, **kwargs) -> int:
        """Decrement the value of a key.

        Args:
            key (str): The key to decrement the value.
            delta (int): The value to decrement.
            **kwargs: Additional arguments.

        Returns:
            int: The value after the decrement.
        """

    @abstractmethod
    async def a_flush(self, **kwargs) -> bool:
        """Delete all keys.

        Args:
            **kwargs: Additional arguments.

        Returns:
            bool: True if all keys were deleted, False otherwise.
        """

    @abstractmethod
    async def a_batch_set(self, data: DictStrSerializable, expire: int = 0, **kwargs) -> bool:
        """Save multiple key-value data.

        Args:
            data (DictStrSerializable): The data to save.
            expire (int): The time to
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was saved, False otherwise.
        """

    @abstractmethod
    async def a_batch_get(self, keys: list[str], **kwargs) -> DictStrSerializable:
        """Get multiple data.

        Args:
            keys (list): The keys to load the data.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: Data loaded.
        """

    @abstractmethod
    async def a_batch_delete(self, keys: list[str], **kwargs) -> bool:
        """Delete multiple data.

        Args:
            keys (list): The keys to delete the data.
            **kwargs: Additional arguments.

        Returns:
            bool: True if the data was deleted, False otherwise.
        """

    @abstractmethod
    async def a_batch_exists(self, keys: list[str], **kwargs) -> DictStrSerializable:
        """Check if multiple data exists.

        Args:
            keys (list): The keys to check if the data exists.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: True if the data exists, False otherwise.
        """

    @abstractmethod
    async def a_batch_ttl(self, keys: list[str], **kwargs) -> DictStrSerializable:
        """Get the expiration time of multiple keys.

        Args:
            keys (list): The keys to get the expiration time.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: The expiration time of the keys.
        """

    @abstractmethod
    async def a_batch_incr(self, keys: list[str], delta: int = 1, **kwargs) -> DictStrSerializable:
        """Increment the value of multiple keys.

        Args:
            keys (list): The keys to increment the value.
            delta (int): The value to increment.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: The value after the increment.
        """

    @abstractmethod
    async def a_batch_decr(self, keys: list[str], delta: int = 1, **kwargs) -> DictStrSerializable:
        """Decrement the value of multiple keys.

        Args:
            keys (list): The keys to decrement the value.
            delta (int): The value to decrement.
            **kwargs: Additional arguments.

        Returns:
            DictStrSerializable: The value after the decrement.
        """
