import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *

root = tb.Window(themename="vapor")
relx = 0.5
rely = 0.1

def subsub():
    global relx, rely
    rely += 0.1
    if rely > 1.0:  # Ensure rely stays within the range [0, 1]
        rely = 0.1
    print(relx, rely)
    button1 = tb.Button(text="great", style="PRIMARY")
    button1.place(relx=relx, rely=rely)

root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False, False)

print(relx, rely)
button = tb.Button(root, text="what is love", style="PRIMARY", command=subsub, takefocus=False)
button.place(relx=0.5, rely=0.1, anchor='ne')

root.mainloop()
