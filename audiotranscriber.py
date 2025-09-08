import whisper

DEFAULT_MODEL = "tiny"

class AudioTranscriber:
    def __init__(self, env_configs={}):
        model_name = env_configs.get("WHISPER_MODEL", DEFAULT_MODEL)
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        self.text_command = result["text"]