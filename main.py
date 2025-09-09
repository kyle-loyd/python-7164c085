from voicerecorder import VoiceRecorder
from audiotranscriber import AudioTranscriber
from environmentmanager import Environment
from modelorchestrator import ModelOrchestrator
from filemanager import FileManager
from logger import Logger

DEFAULT_LOGGING_ROUTE = "console"

if __name__ == "__main__":
    logger = Logger(Environment.get("LOGGING_ROUTE", DEFAULT_LOGGING_ROUTE))
    VoiceRecorder.save_recording()

    whisper = AudioTranscriber()
    recording_path = FileManager.get_recording_filepath()
    transcription = whisper.transcribe(recording_path)

    orchestrator = ModelOrchestrator()
    print(orchestrator.get_response(transcription))