import re


def compact(text: str) -> str:
    """
    Compact a multi-line string into a single-line string.
    """
    return re.sub(' +', ' ', text.replace('\n', ' ')).strip()
