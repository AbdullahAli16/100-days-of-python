# Day: 88(Instructor's solution to Ex: 09 "Shoutouts to Everyone")

import pyttsx3

engine = pyttsx3.init()
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

for name in names:
    print(f"Saying: {name}")
    engine.say(name)
    engine.runAndWait()

engine.stop()
