import logging
import os
import shutil
import stat
from pathlib import Path
from tempfile import mkdtemp
from zipfile import ZipFile

logger = logging.getLogger(__name__)


def tmp_path(prefix: str, suffix: str) -> Path:
    """
    Create a temporary path.
    """
    path = Path(mkdtemp(prefix=f'{prefix}_', suffix=f'_{suffix}'))
    path.mkdir(parents=True, exist_ok=True)  # ensure the path exists
    logger.debug(f'Using temporary path "{path}/"')
    return path


def unzip(archive: Path) -> Path:
    """
    Extract an archive.
    """
    with ZipFile(archive) as archive_file:
        for member_info in archive_file.infolist():
            extracted_path = archive_file.extract(member_info, archive.parent / archive.stem)

            attributes = member_info.external_attr >> 16
            attributes &= stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO  # extract permission bits
            if member_info.is_dir():
                os.chmod(extracted_path, mode=0o755)
            elif attributes:
                os.chmod(extracted_path, mode=attributes)
    return archive


def move(source: Path, destination: Path) -> Path:
    """
    Move a file from source to destination.
    """
    destination.parent.mkdir(parents=True, exist_ok=True)  # create parent folders
    shutil.rmtree(destination, ignore_errors=True)  # remove existing content
    shutil.move(str(source), str(destination))
    return destination
