from filemanager import FileManager
from environmentmanager import ConfigKey
import os
import time

def setup_mock_env(mocker):
    mock_env = mocker.Mock()
    mock_env.get.side_effect = lambda config_key, default=None: {
        ConfigKey.RecordingsDir.value: "./recordings",
        ConfigKey.RetentionCount.value: "5",
        ConfigKey.LogFilePath.value: "./app.log"
    }.get(config_key, default)
    return mock_env

def test_manage_recordings_respects_retention(tmp_path, mocker):
    # Arrange
    mock_env = setup_mock_env(mocker)

    # Act
    fm = FileManager(mock_env)
    fm.recordings_dir = tmp_path
    fm.retention = 2

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

# TODO: Test manage_logger_file and write_log with file mock
# TODO: Test save_recording with soundfile mock
