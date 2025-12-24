import os
import subprocess
import webbrowser

class SystemOps:
    def open_website(self, url):
        """Opens a website in the default browser."""
        if not url.startswith('http'):
            url = 'https://' + url
        webbrowser.open(url)
        return f"Opening {url}"

    def open_app(self, app_name):
        """Attempts to open an application."""
        # This is a basic implementation. For robust app opening, we might need specific paths
        # or use the 'start' command in Windows.
        try:
            # Common apps map
            apps = {
                "chrome": "chrome",
                "notepad": "notepad",
                "calculator": "calc",
                "cmd": "cmd",
                "code": "code"
            }
            
            cmd = apps.get(app_name.lower(), app_name)
            subprocess.Popen(f"start {cmd}", shell=True)
            return f"Opening {app_name}"
            return f"Opening {app_name}"
        except Exception as e:
            return f"Failed to open {app_name}: {e}"

    def play_on_youtube(self, topic):
        """Plays a video on YouTube."""
        try:
            import pywhatkit
            pywhatkit.playonyt(topic)
            return f"Playing {topic} on YouTube"
        except Exception as e:
            return f"Failed to play {topic}: {e}"

    def open_chrome_profile(self, profile_name):
        """Opens Chrome with a specific profile."""
        try:
            # Map names to profile directories
            # You can find these in %LOCALAPPDATA%\Google\Chrome\User Data
            profiles = {
                "vilok": "Profile 1", # Assumption based on request
                "default": "Default",
                "work": "Profile 2"
            }
            
            directory = profiles.get(profile_name.lower(), "Default")
            
            # Using specific path for Chrome is safer when using flags
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            if not os.path.exists(chrome_path):
                 # Fallback for 32-bit or other locations if needed, or rely on PATH
                 chrome_path = "chrome"
            
            subprocess.Popen(f'"{chrome_path}" --profile-directory="{directory}"', shell=True)
            return f"Opening Chrome for {profile_name}"
        except Exception as e:
            return f"Failed to launch Chrome profile {profile_name}: {e}"

if __name__ == "__main__":
    ops = SystemOps()
    ops.open_app("notepad")
