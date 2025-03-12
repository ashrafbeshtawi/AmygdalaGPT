import os
import json
from mistralai import Mistral, models
from dotenv import load_dotenv

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

# API-Key aus der Umgebung abrufen
api_key = os.getenv('MISTRAL_API_KEY')
if not api_key:
    raise ValueError("Missing MISTRAL_API_KEY environment variable")

# Initialisiere den Client
client = Mistral(api_key=api_key)

def get_response(user_prompt: str, short_term_memory: str, model: str = "mistral-tiny") -> str:
    """
    Generiert eine Antwort im JSON-Format mit genau zwei Schlüsseln:
      - user_response: Die finale Antwort auf die Frage des Benutzers.
      - short_term_memory: Ein komprimierter, effizienter Text, der den Kontext der Unterhaltung zusammenfasst.
    
    Beispiel:
      User: "I am Jack, how can I learn math?"
      System: "You can learn math from Khan Academy and other online sources."
      short_term_memory: "username:jack, user wants to learn math, suggestion:khanacademy"
    """
    system_message = (
        "You are a conversation assistant with contextual memory management. Keep these rules for short_term_memory: "
        "1. PRESERVE ALL RELEVANT CONTEXT (names, goals, preferences, ongoing topics)\n"
        "2. ONLY REMOVE INFORMATION WHEN:\n"
        "   - The user explicitly asks to reset\n"
        "   - A COMPLETELY UNRELATED new topic is introduced\n"
        "   - Information becomes objectively irrelevant (e.g., finished task)\n\n"
        
        "Return valid JSON with exactly two keys: 'user_response' and 'short_term_memory'. "
        "Format requirements:\n"
        "- 'user_response': Direct answer to the user's last query\n"
        "- 'short_term_memory': Concise, comma-separated key:value pairs preserving ALL ACTIVE CONTEXT\n\n"
        
        "Examples:\n"
        "Case 1: Continuing topic\n"
        "User: 'I want to learn calculus next'\n"
        "Current memory: 'username:jack, learning_goal:math, level:beginner'\n"
        "New memory: 'username:jack, learning_goal:math, level:beginner, current_focus:calculus'\n\n"
        
        "Case 2: Topic change\n"
        "User: 'Actually, let's talk about cooking instead'\n"
        "Current memory: 'username:jack, learning_goal:math'\n"
        "New memory: 'username:jack, current_topic:cooking'\n\n"
        
        "Return ONLY valid JSON. Never add commentary or formatting."
    )
    
    combined_prompt = (
        f"Previous short term memory: {short_term_memory}\n"
        f"User prompt: {user_prompt}"
    )
    
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": combined_prompt}
        ]
    )
    
    return chat_response.choices[0].message.content.strip()

def main():
    """Hauptfunktion, die den Benutzerprompt entgegennimmt und die generierte JSON-Antwort ausgibt."""
    short_term_memory = ""  # Startet ohne Vorkenntnisse; wird mit jedem Prompt aktualisiert.
    while True:
        user_input = input("Enter Prompt: ")
        try:
            result_json = get_response(user_input, short_term_memory)
            print(result_json)
            
            # Aktualisiere das short_term_memory anhand der KI-Antwort
            parsed = json.loads(result_json)
            short_term_memory = parsed.get("short_term_memory", short_term_memory)
        except Exception as e:
            print(f"Error processing the response: {e}")

if __name__ == "__main__":
    main()
