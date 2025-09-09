from datetime import datetime
import os

DEFAULT_RETENTION_COUNT = 5
DEFAULT_RECORDINGS_DIR = "./recordings"

class FileManager:
    @staticmethod
    def manage_logger_file():
        if not os.path.isfile("app.log"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open("app.log", "w") as f:
                f.write(f"[INFO] [{timestamp}] Log File Created.\n")

    @staticmethod
    def get_recording_filepath(dir=DEFAULT_RECORDINGS_DIR):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording-{timestamp}.wav"
        return f"{dir}/{filename}"

    @staticmethod
    def manage_recordings_dir(dir=DEFAULT_RECORDINGS_DIR):
        if not os.path.isdir(dir):
            os.makedirs(dir)

    @staticmethod
    def manage_recordings(dir=DEFAULT_RECORDINGS_DIR, retention=DEFAULT_RETENTION_COUNT):
        files = [f for f in os.listdir(dir)]
        if len(files) > int(retention):
            files.sort(key=lambda x: os.path.getmtime(f"{dir}/{x}"))
            files_to_delete = files[:-int(retention)]
            for file in files_to_delete:
                os.remove(os.path.join(dir, file))

