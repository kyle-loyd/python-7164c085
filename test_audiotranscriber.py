from audiotranscriber import AudioTranscriber
from environmentmanager import ConfigKey

def test_invalid_model_defaults(mocker):
    # Arrange
    mock_logger = mocker.Mock()
    mock_env = mocker.Mock()
    mock_env.get.side_effect = lambda config_key, default=None: {
        ConfigKey.WhisperModel.value: "average"
    }.get(config_key, default)
    mock_model = mocker.Mock()

    # Act
    at = AudioTranscriber(mock_env, mock_logger)

    # Assert
    assert at.model is not None
    mock_logger.warn.assert_called_once_with("Invalid Whisper model in .env, defaulting to tiny.")

# TODO: Test transcribe with whisper mock
