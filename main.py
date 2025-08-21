import eel
import os

# Match the actual folder name correctly
eel.init("frontend")

# If you want to force open Edge (replace with "Google Chrome" or "Safari" if you prefer)
os.system('open -a "Microsoft Edge" --args --app="http://127.0.0.1:5500/frontend/index.html"')

# Start Eel app
eel.start("index.html", mode="chrome", host="localhost", block=True)
