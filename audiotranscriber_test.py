from unittest.mock import patch, MagicMock
from audiotranscriber import AudioTranscriber

def test_transcribe_sets_text_command():
    fake_model = MagicMock()
    fake_model.transcribe.return_value = {"text": "hello world"}

    with patch("whisper.load_model", return_value=fake_model):
        at = AudioTranscriber()
        at.transcribe("fake_audio.wav")

        fake_model.transcribe.assert_called_once_with("fake_audio.wav")
        assert at.text_command == "hello world"
