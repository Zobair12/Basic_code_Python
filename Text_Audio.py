import pyttsx3

engine = pyttsx3.init()
msg = input("Enter text to speak: ")
speak = int(input("Speak (100-300): "))

engine.setProperty("rate", speak)
engine.say(msg)
engine.runAndWait()