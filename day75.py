# Day: 75(Instructor's solution to Ex: 07 "Clear the Clutter")

import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
    i = i + 1