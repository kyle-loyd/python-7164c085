from abc import ABC, abstractmethod
from enum import Enum

class LogSeverity(Enum):
    Info = "INFO"
    Warning = "WARNING"
    Error = "ERROR"

class LoggerStrategy(ABC):
    @abstractmethod
    def log(self, severity, message):
        pass

class Logger:
    def __init__(self, strategy: LoggerStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: LoggerStrategy):
        self.strategy = strategy

    def log(self, severity, message):
        self.strategy.log(severity, message)

    def info(self, message):
        self.log(LogSeverity.Info.value, message)   

    def warn(self, message):
        self.log(LogSeverity.Warning.value, message)

    def error(self, message):
        self.log(LogSeverity.Error.value, message)

class ConsoleLogger(LoggerStrategy):
    def log(self, severity, message):
        print(f"[{severity}]: {message}")

class FileLogger(LoggerStrategy):
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def log(self, severity, message):
        log = f"[{severity}]: {message}\n"
        self.file_manager.write_log(log)