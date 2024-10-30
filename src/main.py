"""wrapper for Mistral AI"""
import os
from mistralai import Mistral, models
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
    """
    Generates a response using the provided prompt and specified language model.

    Args:
        prompt (str): The input prompt to be used for generating the response.
        model (str, optional): The name of the language model to use. Defaults to "mistral-tiny".

    Returns:
        str: The generated response.
    """
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
    """MAIN FUNCTION"""
    # Example usage
    while True:
        prompt = input('Enter Prompt:')
        try:
            response = get_completion(prompt)
            print(f"Prompt: {prompt}\n")
            print(f"Response: {response}")
        except models.HTTPValidationError as e:
            print(f"Unexpected Payload: {e}")
        except models.SDKError as e:
            print(f"SDK Error: {e}")
if __name__ == "__main__":
    main()
