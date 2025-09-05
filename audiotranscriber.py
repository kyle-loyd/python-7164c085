import whisper

class AudioTranscriber:
    def __init__(self, model_name="tiny"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        self.text_command = result["text"]