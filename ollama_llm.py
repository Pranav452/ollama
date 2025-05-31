#!/usr/bin/env python3
"""
Ollama Local LLM Script
A simple script to interact with a local LLM using Ollama programmatically.
"""

import ollama
import sys

def main():
    """Main function to interact with Ollama LLM"""
    
    # Default model - you can change this to any model you have pulled
    model_name = "gemma3:1b"  # Using the 1B model for faster responses
    
    # Default prompt
    default_prompt = "Hello! Can you tell me what you are and how you can help me?"
    
    # Get prompt from command line args or use default
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = default_prompt
    
    print(f"🤖 Using model: {model_name}")
    print(f"📝 Prompt: {prompt}")
    print("-" * 50)
    
    try:
        # Make the programmatic call to Ollama
        print("🔄 Generating response...")
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        
        # Extract and print the response
        ai_response = response['message']['content']
        print(f"🎯 AI Response:\n{ai_response}")
        
    except ollama.ResponseError as e:
        print(f"❌ Error: {e}")
        print("Make sure you have pulled the model with: ollama pull gemma3:1b")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("Make sure Ollama is running and accessible.")

if __name__ == "__main__":
    main() 