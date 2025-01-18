"""
Utilities for downloading files.
"""
import os
from pathlib import Path
from sys import stderr

import requests
from tqdm import tqdm


def download(url: str, output: Path) -> Path:
    """
    Download a file from a given URL.

    .. note:: Requires the :ref:`download extra <index:download>`.
    """
    print(f'Downloading "{url}"...', file=stderr)
    data_stream = requests.get(url, stream=True, timeout=30)
    total_size = int(data_stream.headers.get('content-length', 0))

    with tqdm(
        total=total_size, leave=False,
        unit='iB', unit_scale=True, unit_divisor=1024,
        disable='GITHUB_ACTIONS' in os.environ,
    ) as progress_bar:
        with open(output, 'wb') as output_file:
            for data in data_stream.iter_content(chunk_size=1024):
                progress_bar.update(output_file.write(data))
    return output
