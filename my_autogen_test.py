import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

# Get current provider
provider = os.getenv('CURRENT_PROVIDER', 'groq').lower()

if provider == 'ollama':
    api_key = "ollama"
    model = os.getenv('OLLAMA_MODEL', 'llama3.2:3b')
    base_url = os.getenv('OLLAMA_API_BASE', 'http://localhost:11434/v1')
    print(f"Using Ollama locally: {model}")
    print("Make sure Ollama is running locally!")
    
elif provider == 'groq':
    api_key = os.getenv('GROQ_API_KEY', 'your_groq_api_key_here')
    
    model = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')
    base_url = "https://api.groq.com/openai/v1"
    print(f"Using Groq: {model}")
    
elif provider == 'google':
    api_key = os.getenv('GOOGLE_API_KEY', 'your_google_api_key_here')
    model = "gpt-3.5-turbo"  
    base_url = None
    print(f"Using Google Gemini setup (Note: May need additional configuration)")
    print("For full Gemini support, consider using Groq or Ollama instead")
    
else:
    api_key = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
    model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    base_url = None
    print(f"Using OpenAI: {model}")

temperature = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
max_tokens = int(os.getenv('OPENAI_MAX_TOKENS', '2000'))

print(f"Temperature: {temperature}")
print(f"Max tokens: {max_tokens}")
print(f"API Key configured: {'Yes' if api_key not in ['your_openai_api_key_here', 'your_groq_api_key_here', 'your_google_api_key_here'] else 'No (please update .env file)'}")

if provider == 'ollama':
    llm_config = {
        "model": model,
        "api_key": api_key,
        "base_url": base_url,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
elif provider == 'groq':
    llm_config = {
        "model": model,
        "api_key": api_key,
        "base_url": base_url,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
else:
    llm_config = {
        "model": model,
        "api_key": api_key,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)
user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config=False
    )

user_proxy.initiate_chat(
    assistant,
    message="Tell me something i don't know?",
)