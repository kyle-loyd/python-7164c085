from dotenv import load_dotenv, dotenv_values
import os

class EnvironmentManager:
    def __init__(self):
        load_dotenv()
        self.configs = dotenv_values(".env")