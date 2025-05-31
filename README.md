# Ollama Local LLM Script

A simple Python script that demonstrates how to interact with a local LLM using Ollama programmatically.

## Prerequisites

1. **Install Ollama**: Download and install from [ollama.ai](https://ollama.ai/)
2. **Python 3.7+**: Make sure you have Python installed

## Setup

1. **Clone this repository** (or download the files)

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull a model** (choose one):
   ```bash
   # Lightweight model (fastest)
   ollama pull gemma3:1b
   
   # Or other options:
   ollama pull gemma3:4b
   ollama pull llama3
   ollama pull mistral
   ollama pull phi
   ```

4. **Start Ollama** (if not running):
   ```bash
   ollama serve
   ```

## Usage

### Run with default prompt:
```bash
python ollama_llm.py
```

### Run with custom prompt:
```bash
python ollama_llm.py "What is the capital of France?"
```

### Multi-word prompts:
```bash
python ollama_llm.py "Explain quantum computing in simple terms"
```

## Example Output

```
🤖 Using model: gemma3:1b
📝 Prompt: Hello! Can you tell me what you are and how you can help me?
--------------------------------------------------
🔄 Generating response...
🎯 AI Response:
Hello! I'm Gemma, a large language model created by Google. I'm designed to be helpful, harmless, and honest...
```

## Customization

- **Change the model**: Edit the `model_name` variable in `ollama_llm.py`
- **Modify the default prompt**: Update the `default_prompt` variable

## Troubleshooting

- **Model not found**: Make sure you've pulled the model with `ollama pull gemma3:1b`
- **Connection error**: Ensure Ollama is running with `ollama serve`
- **Installation issues**: Try `pip install --upgrade ollama`

## Available Models

Popular models you can use:
- `gemma3:1b` - Fastest, smallest
- `gemma3:4b` - Good balance
- `llama3` - High quality
- `mistral` - Good performance
- `phi` - Microsoft's efficient model

Pull any model with: `ollama pull [model-name]` 