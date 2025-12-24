import google.generativeai as genai
from config import GOOGLE_API_KEY

class Brain:
    def __init__(self):
        # We load the key from the environment variable
        api_key = GOOGLE_API_KEY
        if not api_key:
            print("WARNING: GOOGLE_API_KEY not found in .env")
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-flash-latest')

    def think(self, prompt):
        """Sends prompt to LLM and returns response text."""
        try:
            if not getattr(self, 'model', None):
                return "I don't have an API key configured, sir."
            
            # Simple retry logic for 429 (Resource Exhausted)
            import time
            from google.api_core import exceptions
            
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = self.model.generate_content(prompt)
                    return response.text
                except exceptions.ResourceExhausted:
                    if attempt < max_retries - 1:
                        time.sleep(2 * (attempt + 1)) # Exponential-ish backoff
                        continue
                    else:
                        return "I'm currently overloaded with requests, sir. Please try again in a moment."
            
            return "Something went wrong."
        except Exception as e:
            return f"I encountered an error: {str(e)}"

if __name__ == "__main__":
    brain = Brain()
    print(brain.think("Hello, who are you?"))
