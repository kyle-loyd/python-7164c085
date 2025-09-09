from dotenv import dotenv_values

class Environment:
    @staticmethod
    def get(key, default=None):
        return dotenv_values(".env").get(key) or default