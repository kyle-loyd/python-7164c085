import sounddevice as sd
import soundfile as sf

DEFAULT_FILENAME = "recording.wav"
DEFAULT_DURATION = 5 #seconds
DEFAULT_SAMPLE_RATE = 16000 #Hz

class VoiceRecorder:

    def __init__(self, filename="recording.wav", duration=5, sample_rate=16000):
        self.filename = filename
        self.duration = duration
        self.sample_rate = sample_rate

    def record(self):
        self.audio = sd.rec(frames=int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32')
        sd.wait()

    def save(self):
        sf.write(self.filename, self.audio, self.sample_rate)