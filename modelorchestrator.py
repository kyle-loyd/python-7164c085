from environmentmanager import ConfigKey
import ollama

DEFAULT_OLLAMA_MODEL = "mistral"
DEFAULT_MODEL_CONTEXT = "You are my digital assistant."

class ModelOrchestrator:    
    def __init__(self, env, logger):
        self.model_name = env.get(ConfigKey.OllamaModel.value, DEFAULT_OLLAMA_MODEL)
        model_context = env.get(ConfigKey.OllamaContext.value, DEFAULT_MODEL_CONTEXT)
        self.logger = logger
        self.messages = [{"role": "system", "content": model_context}]

    def get_response(self, message):
        self.messages.append({"role": "user", "content": message})
        response = ollama.chat(
            model=self.model_name,
            messages=self.messages
        )
        return response["message"]["content"]
