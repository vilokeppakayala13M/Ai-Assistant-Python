import google.generativeai as genai
import os
from config import GOOGLE_API_KEY

if not GOOGLE_API_KEY:
    print("No API key found in config")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    try:
        print("Listing available models:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
    except Exception as e:
        print(f"Error listing models: {e}")
