import re


def compact(text: str) -> str:
    """
    Removes the unnecessary spaces and end-lines from the text and returns the formatted string.
    """
    return re.sub(' +', ' ', text.replace('\n', ' ')).strip()
