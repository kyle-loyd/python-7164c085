from voicerecorder import VoiceRecorder


def capture_command():
    vr = VoiceRecorder()
    
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


if __name__ == "__main__":
    capture_command()
