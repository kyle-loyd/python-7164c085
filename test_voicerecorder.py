from environmentmanager import ConfigKey
from voicerecorder import VoiceRecorder
import numpy as np

MOCK_DURATION = 1
MOCK_SAMPLE_RATE = 16000
MOCK_DIRECTORY = "test_recordings"
FAKE_AUDIO = np.zeros((16000, 1), dtype='float32')


def test_invalid_duration_defaults(mocker):
    # Arrange
    mock_env = mocker.Mock()
    mock_logger = mocker.Mock()
    mock_env.get.side_effect = lambda config_key, default=None: {
        ConfigKey.RecordingDuration.value: "-10",
        ConfigKey.SampleRate.value: "16000"
    }.get(config_key, default)
    
    # Act
    vr = VoiceRecorder(mock_env, mock_logger)
    
    # Assert
    assert vr.duration == 5
    assert vr.sample_rate == 16000
    mock_logger.warn.assert_called_once_with("Invalid duration in .env, defaulting to 5 seconds.")

def test_invalid_sample_rate_defaults(mocker):
    # Arrange
    mock_env = mocker.Mock()
    mock_logger = mocker.Mock()
    mock_env.get.side_effect = lambda config_key, default=None: {
        ConfigKey.RecordingDuration.value: "5",
        ConfigKey.SampleRate.value: "8000"
    }.get(config_key, default)
    
    # Act
    vr = VoiceRecorder(mock_env, mock_logger)
    
    # Assert
    assert vr.duration == 5
    assert vr.sample_rate == 16000
    mock_logger.warn.assert_called_once_with("Invalid sample rate in .env, defaulting to 16000 Hz.")

# TODO: Test get_recording with sounddevice mock