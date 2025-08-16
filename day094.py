# Day: 94 (Ex: 11 "Drink water Reminder")

import tkinter as tk, winsound, threading

root= tk.Tk()
root.withdraw()

def show_reminder():
    
    popup=tk.Toplevel(root)
    popup.geometry("350x120+500+300")        # Window displays in the center
    popup.title("Reminder")                  # Title of the window
    popup.attributes("-topmost",True)        # Displays on top of all windows
    popup.resizable(False,False)             # No resizing

    popup.bind("<Escape>", lambda e: (print("Reminder program closed."), root.destroy()))
    content=tk.Label(popup,text="Time to drink water",font=("Segoe UI", 18, "bold"))
    content.pack(padx=20, pady=20)          # Vertical and Horizontal Padding for the text

    def play_sound():
        winsound.Beep(500,3000)

    threading.Thread(target=play_sound,daemon=True).start()
    popup.after(3000,popup.destroy)
    root.after(7200000,show_reminder)
    

show_reminder()

root.mainloop()