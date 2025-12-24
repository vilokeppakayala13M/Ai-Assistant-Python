import time
import sys
from voice.listener import Listener
from voice.speaker import Speaker
from brain.llm_interface import Brain
from skills.system_ops import SystemOps
from config import WAKE_WORD

def main():
    print("Initializing Avinya...")
    listener = Listener()
    speaker = Speaker()
    brain = Brain()
    sys_ops = SystemOps()
    
    speaker.speak("Systems online. How can I help you?")
    print(f"Listening for wake word '{WAKE_WORD}'...")

    while True:
        try:
            print("Listening...", end="\r") # Overwrite line to avoid spam
            text = listener.listen()
        except KeyboardInterrupt:
            break
        
        if text:
            print(f"\nUser: {text}") # Newline to clear the \r
            # Simple interaction logic
            if WAKE_WORD in text:
                # Remove wake word logic if you want continuous conversation or just respond
                # For now, we respond to everything if it hears something, or filtered by wake word
                pass
            
            # Check for commands
            command_keywords = ["open", "start", "launch", "run"]
            triggered_keyword = next((kw for kw in command_keywords if kw in text), None)

            if triggered_keyword and ("google" in text or "youtube" in text):
                if "google" in text:
                    response = sys_ops.open_website("google.com")
                elif "youtube" in text:
                    response = sys_ops.open_website("youtube.com")
            elif triggered_keyword:
                # Try to extract app name
                words = text.split()
                try:
                    idx = words.index(triggered_keyword)
                    
                    # Check for "open id {name}"
                    if triggered_keyword == "open" and idx + 2 < len(words) and words[idx+1] == "id":
                        profile_name = words[idx+2]
                        response = sys_ops.open_chrome_profile(profile_name)
                    
                    # Check for "play/start {song_name}"
                    elif (triggered_keyword in ["play", "start"]) and idx + 1 < len(words):
                        # If "song" is explicitly mentioned
                        if "song" in words[idx+1:]:
                            try:
                                song_idx = words.index("song", idx)
                                song_name = " ".join(words[song_idx+1:])
                                if song_name.strip():
                                    response = sys_ops.play_on_youtube(song_name)
                                else:
                                    response = "Play what song, sir?"
                            except:
                                response = "Play what song, sir?"
                        else:
                            # Assume it's a song/media request if just "play X"
                            # But be careful not to conflict with "start chrome" which is handled by open_app
                            # core 'start' logic falls here if not caught above. 
                            # 'open' is handled separately for apps? No, open/start are in same triggered_keyword list.
                            
                            # Existing app logic is below this block.
                            # We need to distinguish "start chrome" (app) from "play alone part 2" (song).
                            # Simple heuristic: Check if the text matches a known app? 
                            # Or, if verb is 'play', always music. If 'start', maybe app.
                            
                            if triggered_keyword == "play":
                                song_name = " ".join(words[idx+1:])
                                response = sys_ops.play_on_youtube(song_name)
                            else:
                                # It's 'start' or 'launch' or 'run' -> might be app
                                # Fall through to app logic
                                pass # Continue to next elif checking for app name

                    # App launching logic
                    if idx + 1 < len(words) and triggered_keyword != "play": # Don't open apps with 'play'
                        app_name = " ".join(words[idx+1:]) # Join rest of string for multi-word apps
                        response = sys_ops.open_app(app_name)
                    elif triggered_keyword != "play" and "response" not in locals():
                         response = "Open what, sir?"
                except:
                    response = "I couldn't quite catch what to open."
            elif "stop" in text or "exit" in text:
                speaker.speak("Shutting down. Goodbye.")
                break
            else:
                # Ask the brain
                response = brain.think(text)
            
            print(f"Avinya: {response}")
            speaker.speak(response)
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()
