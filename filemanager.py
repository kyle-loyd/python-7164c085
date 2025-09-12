from datetime import datetime
from environmentmanager import ConfigKey
import os
import soundfile as soundfile

DEFAULT_RETENTION_COUNT = 5
DEFAULT_RECORDINGS_DIR = "./recordings"
DEFAULT_LOG_FILE_PATH = "./app.log"

class FileManager:
    def __init__(self, env):
        self.recordings_dir = env.get(ConfigKey.RecordingsDir.value, DEFAULT_RECORDINGS_DIR)
        self.log_file_path = env.get(ConfigKey.LogFilePath.value, DEFAULT_LOG_FILE_PATH)
        self.retention = int(env.get(ConfigKey.RetentionCount.value))

    def set_logger(self, logger):
        self.logger = logger

    def manage_logger_file(self):
        if not os.path.isfile(self.log_file_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open(self.log_file_path, "w") as f:
                f.write(f"[INFO] [{timestamp}] Log File Created.\n")

    def write_log(self, log):
        self.manage_logger_file()
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(log)

    def get_recording_filepath(self) -> str:
        if not os.path.isdir(self.recordings_dir):
            os.makedirs(self.recordings_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording-{timestamp}.wav"
        return f"{self.recordings_dir}/{filename}"
        
    def manage_recordings(self):
        if self.retention <= 0:
            self.retention = DEFAULT_RETENTION_COUNT
            self.logger.warn(f"Invalid retention count in .env, defaulting to {DEFAULT_RETENTION_COUNT} recordings.")
        
        files = [f for f in os.listdir(self.recordings_dir)]
        if len(files) > self.retention:
            files.sort(key=lambda x: os.path.getmtime(f"{self.recordings_dir}/{x}"))
            files_to_delete = files[:-self.retention]
            for file in files_to_delete:
                os.remove(os.path.join(self.recordings_dir, file))

    def save_recording(self, audio):
        filepath = self.get_recording_filepath()
        soundfile.write(filepath, audio, self.sample_rate)
