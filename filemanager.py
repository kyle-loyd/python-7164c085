import os

class FileManager:
    def __init__(self):
        self.retention_count = os.environ.get("COMMAND_RETENTION_COUNT", 5)
        self.recordings_dir = os.environ.get("RECORDINGS_DIR", "./recordings")

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

