import pyttsx3
import threading

class Speaker:
    def __init__(self, rate=175):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.lock = threading.Lock()

    def speak(self, text):
        """Speaks the given text."""
        # pyttsx3 is not thread-safe by default, so we lock
        with self.lock:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except RuntimeError:
                 # In case the loop is already running
                pass

    def stop(self):
        self.engine.stop()

if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("Hello sir, I am ready.")
