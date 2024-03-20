"""
# Backends

This module contains the backends for the caching system.
The backends are responsible for the actual storage and retrieval of the cached data.
The backends are designed to be interchangeable, so that the caching system can be used with different storage systems,
such as a `redis` server, a `memcached` server, or a simple file-based cache.
"""

__all__ = [
    "AbstractBackend",
]

from .abstract import Abstract as AbstractBackend
