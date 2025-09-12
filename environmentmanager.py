from dotenv import dotenv_values
from enum import Enum

class ConfigKey(Enum):
    RetentionCount = "COMMAND_RETENTION_COUNT", 
    RecordingsDir = "RECORDINGS_DIR", 
    RecordingDuration = "RECORDING_DURATION", 
    SampleRate = "SAMPLE_RATE", 
    WhisperModel = "WHISPER_MODEL", 
    OllamaModel = "OLLAMA_MODEL", 
    OllamaContext = "OLLAMA_CONTEXT", 
    LogFilePath = "LOG_FILE_PATH", 
    LoggingRoute = "LOGGING_ROUTE"

class Environment:
    def __init__(self):
        self.configs = dotenv_values(".env")
    
    def get(self, config_key, default=None):
        return self.configs.get(config_key.value) or default