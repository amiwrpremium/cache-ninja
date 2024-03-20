"""
# Utils

This module contains utility functions for the application.

## Functions
    - slugify: Convert a string to a slug.
"""

import unicodedata
import re


def slugify(s, allow_unicode: bool = False):
    """
    Convert a string to a slug.

    Args:
        s (str): The string to convert.
        allow_unicode (bool): Whether to allow unicode characters.

    Returns:
        str: The slugified string.

    Example:
    ```python
        from cache_ninja.utils import slugify

        slugify("Hello, World!")
        # Output: 'hello-world'
    ```
    """
    s = str(s)

    if allow_unicode:
        s = unicodedata.normalize('NFKC', s)
    else:
        s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')

    # s = re.sub(r'[^\w\s-]', '', s).strip().lower()
    # return re.sub(r'[-\s]+', '-', s)

    s = re.sub(r"[^\w\s-]", "", s.lower())
    return re.sub(r"[-\s]+", "-", s).strip("-_")
