import re

def compact(text: str) -> str:
    return re.sub(' +', ' ', text.replace('\n', ' ')).strip()
