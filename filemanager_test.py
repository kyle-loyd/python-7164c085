import os
import time
import tempfile
from filemanager import FileManager

def test_manage_recordings_dir_creates(tmp_path):
    fm = FileManager()
    fm.recordings_dir = tmp_path / "recordings"

    assert not fm.recordings_dir.exists()

    fm.manage_recordings_dir()

    assert fm.recordings_dir.exists()
    assert fm.recordings_dir.is_dir()


def test_manage_recordings_respects_retention(tmp_path):
    fm = FileManager()
    fm.recordings_dir = tmp_path
    fm.retention_count = 2

    files = []
    for i in range(4):
        f = tmp_path / f"file{i}.wav"
        f.write_text("dummy")
        files.append(f)
        os.utime(f, (time.time() + i, time.time() + i))

    fm.manage_recordings()

    remaining = list(os.listdir(tmp_path))
    assert len(remaining) == 2
    assert set(remaining) == {"file2.wav", "file3.wav"}
