import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('MISTRAL_API_KEY')

if not api_key:
    raise ValueError("Missing MISTRAL_API_KEY environment variable")

# Initialize the client
client = Mistral(api_key=api_key)

def get_completion(prompt: str, model: str = "mistral-tiny") -> str:
    
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    
    return chat_response.choices[0].message.content

def main():
    # Example usage
    while True:
        prompt = input('Enter Prompt:')
        try:
            response = get_completion(prompt)
            print(f"Prompt: {prompt}\n")
            print(f"Response: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()