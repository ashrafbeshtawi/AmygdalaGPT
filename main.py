import os
from mistralai.client import MistralClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('MISTRAL_API_KEY')

if not api_key:
    raise ValueError("Missing MISTRAL_API_KEY environment variable")

# Initialize the client
client = MistralClient(api_key=api_key)

def get_completion(prompt: str, model: str = "mistral-tiny") -> str:
    
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": "What is the best French cheese?",
            },
        ]
    )
    
    return chat_response.choices[0].message.content

def main():
    # Example usage
    prompt = "Explain quantum computing in simple terms"
    try:
        response = get_completion(prompt)
        print(f"Prompt: {prompt}\n")
        print(f"Response: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()