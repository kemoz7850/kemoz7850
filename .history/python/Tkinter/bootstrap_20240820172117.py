import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
root = tb.Window(themename="vapor")
root.title("Accounts")
root.iconbitmap('skills.ico')
windowWidth = 400
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(False,False)
no_border_button = tk.Button(root, text="No Border", bd=0)
    no_border_button.pack(padx=10, pady=10)
root.mainloop()