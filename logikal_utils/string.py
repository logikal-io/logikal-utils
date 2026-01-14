"""
Utilities for managing strings.
"""
import re


def compact(text: str) -> str:
    """
    Return the formatted string.
    """
    return re.sub(' +', ' ', text.replace('\n', ' ')).strip()
