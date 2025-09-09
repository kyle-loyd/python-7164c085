import ollama
from environmentmanager import Environment

DEFAULT_OLLAMA_MODEL = "mistral"
DEFAULT_MODEL_CONTEXT = "You are my digital assistant."

class ModelOrchestrator:    
    def __init__(self):
        self.model_name = Environment.get("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL)
        model_context = Environment.get("OLLAMA_CONTEXT", DEFAULT_MODEL_CONTEXT)
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
