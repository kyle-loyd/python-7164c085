from filemanager import FileManager
from environmentmanager import Environment, get
import sounddevice as device
import soundfile as file

DEFAULT_DURATION = 5
DEFAULT_SAMPLE_RATE = 16000

class VoiceRecorder:        
    @staticmethod
    def save_recording():
        duration = int(Environment.get("RECORDING_DURATION", DEFAULT_DURATION))
        sample_rate = int(Environment.get("SAMPLE_RATE", DEFAULT_SAMPLE_RATE))
        recordings_dir = Environment.get("RECORDINGS_DIR")

        audio = device.rec(frames=int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        device.wait()
        path = FileManager.manage_recordings_dir(recordings_dir)
        file.write(path, audio, sample_rate)