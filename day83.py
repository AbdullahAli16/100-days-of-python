# Day: 83(Ex: 09 "Shoutouts for Everyone")

import win32com.client as wc
print(dir(wc))
names=["Abdullah","Sarim","Afzal","Saadan"]

voice=wc.Dispatch("SAPI.SpVoice")

print(dir(voice))
for name in names:
    voice.speak(f"Shout-out to {name}")
    
