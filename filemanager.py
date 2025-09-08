from datetime import datetime
import os

DEFAULT_RETENTION_COUNT = 5
DEFAULT_RECORDINGS_DIR = "./recordings"

class FileManager:
    def __init__(self, env_configs={}):
        self.retention_count = int(env_configs.get("COMMAND_RETENTION_COUNT", DEFAULT_RETENTION_COUNT))
        self.recordings_dir = env_configs.get("RECORDINGS_DIR", DEFAULT_RECORDINGS_DIR)
        formatted_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording-{formatted_timestamp}.wav"
        self.full_path = f"{self.recordings_dir}/{filename}"

    def manage_recordings_dir(self):
        if not os.path.isdir(self.recordings_dir):
            os.makedirs(self.recordings_dir)

    def manage_recordings(self):
        files = [f for f in os.listdir(self.recordings_dir)]
        if len(files) > int(self.retention_count):
            files.sort(key=lambda x: os.path.getmtime(f"{self.recordings_dir}/{x}"))
            files_to_delete = files[:-int(self.retention_count)]
            for file in files_to_delete:
                os.remove(os.path.join(self.recordings_dir, file))

