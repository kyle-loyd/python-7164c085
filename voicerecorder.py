from datetime import datetime
import sounddevice as device
import soundfile as file
import os

class VoiceRecorder:

    def __init__(self):
        destination_dir = os.environ.get("RECORDINGS_DIR", "./recordings")
        formatted_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording-{formatted_timestamp}.wav"

        self.full_path = f"{destination_dir}/{filename}"
        self.duration = os.environ.get("RECORDING_DURATION", 5)
        self.sample_rate = os.environ.get("SAMPLE_RATE", 16000)

    def record(self):
        self.audio = device.rec(frames=int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32')
        device.wait()

    def save(self):
        file.write(self.full_path, self.audio, self.sample_rate)