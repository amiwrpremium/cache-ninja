"""
# Serializers

This module contains the serializers for the caching system.
The serializers are responsible for the serialization and deserialization of the cached data.
The serializers are designed to be interchangeable, so that the caching system can be used with different data formats,
such as `json`, `msgpack`, or `pickle`.

"""

__all__ = [
    "AbstractSerializer",
]

from .abstract import Abstract as AbstractSerializer
