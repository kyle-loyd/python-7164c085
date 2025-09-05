from voicerecorder import VoiceRecorder
from audiotranscriber import AudioTranscriber

def capture_command():
    vr = VoiceRecorder()
    
    print("Recording voice command...")
    try:
        vr.record()
    except Exception as record_exception:
        print(f"Recording failed: {record_exception}")
        return
    print("Voice command successfully recorded.")
    
    try:
        vr.save()
    except Exception as save_exception:
        print(f"Saving failed: {save_exception}")
        return
    print("Voice command successfully saved.")

def transcribe_command():
    at = AudioTranscriber()
    try:
        at.transcribe(vr.filename)
    except Exception as transcribe_exception:
        print(f"Transcription failed: {transcribe_exception}")
        return
    print("Command: " + at.text_command)


if __name__ == "__main__":
    capture_command()
