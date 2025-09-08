from voicerecorder import VoiceRecorder
from audiotranscriber import AudioTranscriber
from filemanager import FileManager
from environmentmanager import EnvironmentManager
from modelorchestrator import ModelOrchestrator


def capture_command(configs):
    fm = FileManager(configs)
    try:
        fm.manage_recordings_dir()
    except Exception as dir_exception:
        print(f"Directory management failed: {dir_exception}")
        return
    print("Recordings directory is ready.")

    vr = VoiceRecorder(configs)
    print("Recording voice command...")
    try:
        vr.record()
    except Exception as record_exception:
        print(f"Recording failed: {record_exception}")
        return
    print("Voice command successfully recorded.")
    
    try:
        vr.save(fm.full_path)
    except Exception as save_exception:
        print(f"Saving failed: {save_exception}")
        return
    print("Voice command successfully saved.")

    try:
        fm.manage_recordings()
    except Exception as manage_exception:
        print(f"File management failed: {manage_exception}")
        return
    print("Recording cleanup complete.")

    return fm.full_path

def transcribe_command(path, configs):
    at = AudioTranscriber(configs)
    try:
        at.transcribe(path)
    except Exception as transcribe_exception:
        print(f"Transcription failed: {transcribe_exception}")
        return
    return at.text_command


if __name__ == "__main__":
    env = EnvironmentManager()
    recording_filepath = capture_command(env.configs)
    transcription = transcribe_command(path=recording_filepath, configs=env.configs)
    orchestrator = ModelOrchestrator(env.configs)
    print(orchestrator.get_response(transcription))