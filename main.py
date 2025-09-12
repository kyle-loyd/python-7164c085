from voicerecorder import VoiceRecorder
from audiotranscriber import AudioTranscriber
from environmentmanager import Environment
from enums import LogSeverity, ConfigKey
from modelorchestrator import ModelOrchestrator
from filemanager import FileManager
from logger import Logger

DEFAULT_LOGGING_ROUTE = "console"

if __name__ == "__main__":
    env = Environment()
    fm = FileManager(env)
    log_route = env.get(ConfigKey.LoggingRoute, DEFAULT_LOGGING_ROUTE)
    logger = Logger(log_route, fm)
    fm.set_logger(logger)

    vr = VoiceRecorder()
    recording = vr.get_recording()

    
    fm.save_recording(recording)

    whisper = AudioTranscriber()
    recording_path = FileManager.get_recording_filepath()
    transcription = whisper.transcribe(recording_path)

    orchestrator = ModelOrchestrator()
    print(orchestrator.get_response(transcription))