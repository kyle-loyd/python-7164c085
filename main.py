from voicerecorder import VoiceRecorder
from audiotranscriber import AudioTranscriber
from filemanager import FileManager
from dotenv import load_dotenv

def load_env_vars():
    if not load_dotenv():
        print("No environment variables set within \".env\" file")
        exit(1)

def capture_command():
    vr = VoiceRecorder()
    fm = FileManager()

    print("Recording voice command...")
    try:
        vr.record()
    except Exception as record_exception:
        print(f"Recording failed: {record_exception}")
        return
    print("Voice command successfully recorded.")
    
    try:
        fm.manage_recordings_dir()
    except Exception as dir_exception:
        print(f"Directory management failed: {dir_exception}")
        return
    print("Recordings directory is ready.")

    try:
        vr.save()
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

    return vr.full_path

def transcribe_command(filepath):
    at = AudioTranscriber()
    try:
        at.transcribe(filepath)
    except Exception as transcribe_exception:
        print(f"Transcription failed: {transcribe_exception}")
        return
    print("Command: " + at.text_command)



if __name__ == "__main__":
    load_env_vars()
    recording_filepath = capture_command()
    transcribe_command(recording_filepath)
