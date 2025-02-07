from chatgpt_memory.llm_client.config import LLMClientConfig


class ChatGPTConfig(LLMClientConfig):
    temperature: float = 0
    model_name: str = "gpt-4"
    max_retries: int = 6
    max_tokens: int = 2500 # 256
    verbose: bool = True
