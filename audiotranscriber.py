from environmentmanager import ConfigKey
import whisper

# https://pypi.org/project/openai-whisper/
DEFAULT_WHISPER_MODEL = "tiny"
valid_whisper_models = ["tiny", "base", "small", "medium", "large", "turbo"]

class AudioTranscriber:
    def __init__(self, env, logger):
        self.logger = logger
        whisper_model = env.get(ConfigKey.WhisperModel.value, DEFAULT_WHISPER_MODEL)
        if whisper_model not in valid_whisper_models:
            whisper_model = DEFAULT_WHISPER_MODEL
            logger.warn(f"Invalid Whisper model in .env, defaulting to {DEFAULT_WHISPER_MODEL}.")
        self.model = whisper.load_model(whisper_model)

    def transcribe(self, audio_path) -> str:
        return self.model.transcribe(audio_path)["text"]