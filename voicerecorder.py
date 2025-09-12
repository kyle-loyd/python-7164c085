from environmentmanager import ConfigKey
import sounddevice as device

DEFAULT_DURATION = 5
DEFAULT_SAMPLE_RATE = 16000

class Recording:
    def __init__(self, audio, samplerate):
        self.audio = audio
        self.samplerate = samplerate

class VoiceRecorder:        
    def __init__(self, env, logger):
        self.duration = int(env.get(ConfigKey.RecordingDuration.value))
        if self.duration <= 0:
            self.duration = DEFAULT_DURATION
            logger.warn(f"Invalid duration in .env, defaulting to {DEFAULT_DURATION} seconds.")

        self.sample_rate = int(env.get(ConfigKey.SampleRate.value))
        if self.sample_rate < 16000:
            self.sample_rate = DEFAULT_SAMPLE_RATE
            logger.warn(f"Invalid sample rate in .env, defaulting to {DEFAULT_SAMPLE_RATE} Hz.")
    
    def get_recording(self):
        audio = device.rec(frames=int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32')
        device.wait()
        return Recording(audio, self.sample_rate)    