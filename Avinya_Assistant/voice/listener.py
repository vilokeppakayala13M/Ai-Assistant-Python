import speech_recognition as sr
import time

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def listen(self):
        """Listens for audio and returns the string."""
        try:
            with self.microphone as source:
                # timeout: seconds to wait before giving up if no speech is detected
                # phrase_time_limit: max seconds to record
                audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=10) # Set timeout to None for continuous listening without errors
            
            print("Processing Audio...")
            text = self.recognizer.recognize_google(audio)
            print(f"User said: {text}")
            text = text.lower()
            
            # Common misheard variations
            misheard = ["avenger", "avania", "lavinya", "avinash", "avanya"]
            for m in misheard:
                if m in text:
                    text = text.replace(m, "avinya")
            
            return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

if __name__ == "__main__":
    listener = Listener()
    while True:
        result = listener.listen()
        if result:
            print(f"Caught: {result}")
