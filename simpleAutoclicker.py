import threading
import tkinter as tk
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Key, Controller as KeyboardController
import time

# Initialize mouse and keyboard controllers
mouse = MouseController()
keyboard = KeyboardController()

# Define the hotkey
hotkey = KeyCode.from_char('f')

# Initialize the delay
delay = 0.1

# Initialize clicking state
clicking = False

def on_press(key):
    global clicking
    if key == hotkey:
        clicking = not clicking

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left)
            time.sleep(delay)

def set_delay():
    global delay
    delay = float(delay_entry.get())/1000

# Create a tkinter window
root = tk.Tk()
root.title("Python Autoclicker")

# Create an instruction label
instruction_label = tk.Label(root, text="Press 'f' to start/stop the autoclicker")
instruction_label.pack()

# Create an entry field for delay
delay_entry = tk.Entry(root)
delay_entry.pack()
delay_entry.insert(0, "Enter ms between clicks")

# Create a button to set the delay
delay_button = tk.Button(root, text="Set delay", command=set_delay)
delay_button.pack()

# Start the keyboard listener
listener = Listener(on_press=on_press)
listener.start()

# Start the clicker
clicker_thread = threading.Thread(target=clicker)
clicker_thread.start()

# Start the tkinter main loop
root.mainloop()
