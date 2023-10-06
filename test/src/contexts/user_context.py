from instaloader import Instaloader

L = Instaloader()

try:
    L.load_session_from_file("session-luciano.alcantara.dev", r"/home/luciano/.config/instaloader/session-luciano.alcantara.dev") #1st argument should be username and 2nd argument should be the saved file location
    print("Logged In Successfully")
except Exception as e:
    print("Error", e)