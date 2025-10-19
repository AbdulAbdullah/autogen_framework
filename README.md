# AI Agent Project

A learning project for building AI agents using Autogen with free LLM providers.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- API key from a supported LLM provider (see [Supported Providers](#supported-providers))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Agents
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv autogenenv
   
   # On Windows (Git Bash)
   source autogenenv/Scripts/activate
   
   # On macOS/Linux
   source autogenenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and preferences
   ```

5. **Run the test agent**
   ```bash
   python test.py
   ```

## 🔧 Configuration

### Environment Variables

The project uses a `.env` file for configuration. Key variables include:

- `CURRENT_PROVIDER`: Choose your LLM provider (`groq`, `google`, `ollama`)
- `GROQ_API_KEY`: Your Groq API key (if using Groq)
- `GOOGLE_API_KEY`: Your Google API key (if using Gemini)
- `OPENAI_TEMPERATURE`: Temperature setting for response creativity (0.0-1.0)
- `OPENAI_MAX_TOKENS`: Maximum tokens per response

### Supported Providers

#### 🆓 Free Options (Recommended for Learning)

1. **Groq** (Recommended)
   - **Cost**: Free tier with 100 requests/day
   - **Speed**: Very fast inference
   - **Models**: Llama 3.1, Mixtral, Gemma
   - **Setup**: Get API key from [console.groq.com](https://console.groq.com)

2. **Ollama** (Local)
   - **Cost**: Completely free
   - **Privacy**: Runs locally
   - **Models**: Llama, Mistral, CodeLlama
   - **Setup**: Install from [ollama.ai](https://ollama.ai)

3. **Google Gemini**
   - **Cost**: Free tier available
   - **Models**: Gemini Pro
   - **Setup**: Get API key from [aistudio.google.com](https://aistudio.google.com)

### Switching Providers

Simply change the `CURRENT_PROVIDER` in your `.env` file:

```env
# For Groq (cloud-based, fast)
CURRENT_PROVIDER=groq

# For Ollama (local, private)
CURRENT_PROVIDER=ollama

# For Google Gemini
CURRENT_PROVIDER=google
```

## 📁 Project Structure

```
Agents/
├── .env                    # Environment variables (create from .env.example)
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
├── my_autogen_test.py               # Main test agent script
├── autogenenv/           # Virtual environment (ignored by git)
└── README.md            # This file
```

## 🧪 Usage Examples

### Basic Agent Conversation

```python
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os

load_dotenv()

# Configure LLM
llm_config = {
    "model": os.getenv('OPENAI_MODEL', 'llama-3.1-8b-instant'),
    "api_key": os.getenv('GROQ_API_KEY'),
    "base_url": "https://api.groq.com/openai/v1",
}

# Create agents
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Hello! Can you help me understand how AI agents work?"
)
```

## 🛠️ Development

### Code Quality

The project includes tools for maintaining code quality:

```bash
# Format code
black .

# Check code style
flake8 .

# Run tests
pytest
```

### Dependencies

Core dependencies include:
- `pyautogen`: Core Autogen library
- `python-dotenv`: Environment variable management
- `openai`: OpenAI client (used by various providers)
- `tiktoken`: Token counting
- Additional tools for web scraping, testing, and data processing

## 🎯 Learning Resources

- [Autogen Documentation](https://microsoft.github.io/autogen/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Google AI Studio](https://aistudio.google.com/)
- [Ollama Documentation](https://ollama.ai/docs)

## 🤝 Contributing

This is a learning project! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is for educational purposes. See LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`

2. **API Key Issues**
   - Check `.env` file configuration
   - Verify API key is valid and has sufficient quota

3. **Model Not Found**
   - For Ollama: Ensure model is pulled (`ollama pull llama3.2:3b`)
   - For cloud providers: Check model name in documentation

### Getting Help

- Check the [Issues](../../issues) section
- Review provider documentation
- Ensure all dependencies are properly installed

## 🔄 Updates

To update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

To update the project:
```bash
git pull origin main
pip install -r requirements.txt
```

---

**Happy Learning!** 🎉

Start with Groq for quick setup, then explore Ollama for local development, and experiment with different agent configurations!