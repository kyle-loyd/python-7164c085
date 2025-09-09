from abc import ABC, abstractmethod
from filemanager import FileManager, manage_logger_file

class LoggerStrategy(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class Logger:
    def __init__(self, strategy: LoggerStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: LoggerStrategy):
        self.strategy = strategy

    def log(self, severity: str, message: str):
        self.strategy.log(severity, message)

class ConsoleLogger(LoggerStrategy):
    def log(self, severity: str, message: str):
        print(f"[{severity}]: {message}")

class FileLogger(LoggerStrategy):
    def __init__(self, file_path: str):
        FileManager.manage_logger_file()
        self.file_path = file_path

    def log(self, severity: str, message: str):
        with open(self.file_path, 'a') as log_file:
            log_file.write(f"[{severity}]: {message}\n")