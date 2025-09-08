import ollama
from time import sleep

DEFAULT_OLLAMA_MODEL = "mistral"
DEFAULT_MODEL_CONTEXT = "You are my digital assistant."

class ModelOrchestrator:    
    def __init__(self, env_configs={}):
        self.model_name = env_configs.get("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL)
        model_context = env_configs.get("OLLAMA_CONTEXT", DEFAULT_MODEL_CONTEXT)
        self.messages = [{"role": "system", "content": model_context}]
        print(self.messages)

    def get_response(self, message):
        print(self.messages)
        self.messages.append({"role": "user", "content": message})
        print(self.messages)
        response = ollama.chat(
            model=self.model_name,
            messages=self.messages
        )
        return response["message"]["content"]
