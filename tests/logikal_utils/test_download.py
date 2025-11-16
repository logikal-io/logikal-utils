from pathlib import Path

from logikal_utils.download import download


def test_download(tmp_path: Path) -> None:
    logikal_index = download('https://github.com/logikal-io', tmp_path / 'index.html')
    assert 'Creating perfect digital experiences' in logikal_index.read_text()
