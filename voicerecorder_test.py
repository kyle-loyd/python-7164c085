import numpy as np
from unittest.mock import patch
from voicerecorder import VoiceRecorder

def test_record_creates_audio_array():
    vr = VoiceRecorder()

    fake_audio = np.zeros((16000, 1), dtype='float32')

    with patch("sounddevice.rec", return_value=fake_audio) as mock_rec, \
         patch("sounddevice.wait") as mock_wait:

        vr.record()

        mock_rec.assert_called_once()
        mock_wait.assert_called_once()
        assert isinstance(vr.audio, np.ndarray)
        assert vr.audio.shape == (16000, 1)

def test_save_writes_file(tmp_path):
    vr = VoiceRecorder()
    vr.audio = np.zeros((16000, 1), dtype='float32')

    with patch("soundfile.write") as mock_write:
        vr.save()
        mock_write.assert_called_once()
        args, kwargs = mock_write.call_args
        assert args[0] == vr.full_path
        assert isinstance(args[1], np.ndarray)
        assert args[2] == vr.sample_rate
