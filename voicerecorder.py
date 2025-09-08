import sounddevice as device
import soundfile as file

DEFAULT_DURATION = 5
DEFAULT_SAMPLE_RATE = 16000

class VoiceRecorder:

    def __init__(self, env_configs={}):
        self.duration = int(env_configs.get("RECORDING_DURATION", DEFAULT_DURATION))
        self.sample_rate = int(env_configs.get("SAMPLE_RATE", DEFAULT_SAMPLE_RATE))

    def record(self):
        self.audio = device.rec(frames=int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32')
        device.wait()

    def save(self, path):
        file.write(path, self.audio, self.sample_rate)