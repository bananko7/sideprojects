'''
Pyesight is a GUI tool to keep your eyes healthy by reminding you to take a break from the screen every 20 minutes.

'''

import tkinter as tk
from tkinter import simpledialog
import winsound
import threading

def beep():
    # Beep at 2500 Hz for 1 second
    winsound.Beep(1000, 400)  
    winsound.Beep(500, 400)
    winsound.Beep(1000, 400)  
    winsound.Beep(500, 400)
update_id = None

def start_timer():
    global remaining, update_id
    remaining = interval
    if update_id is not None:
        root.after_cancel(update_id)
    update_label()

def update_label():
    global remaining, update_id
    if remaining > 0:
        remaining -= 1
        minutes, seconds = divmod(remaining, 60)
        time_label.config(text=f"{int(minutes)}:{int(seconds):02}")
        update_id = root.after(1000, update_label)
    else:
        end_timer()
def end_timer():
    time_label.config(text="Beeping, take a break!")
    root.update_idletasks()  # Update the GUI
    beep()
    time_label.config(text="0:00")
    start_timer()

def set_interval():
    global interval
    interval = simpledialog.askfloat("Input", "Enter interval in minutes", parent=root)
    interval *= 60  # convert minutes to seconds
    start_timer()

root = tk.Tk()
root.title("Pyesight")
interval = 20 * 60  # 20 minutes in seconds
remaining = 0

# Set window size
window_width = 450
window_height = 250
root.geometry(f"{window_width}x{window_height}")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Set position
root.geometry(f"+{position_right}+{position_top}")

button = tk.Button(root, text='Set Interval', command=set_interval, font=('Helvetica', '20', 'bold'))
button.place(relx=0.5, rely=0.4, anchor='center')

time_label = tk.Label(root, text=str(remaining), font=('Helvetica', '20', 'bold'))
time_label.place(relx=0.5, rely=0.6, anchor='center')

start_timer()

root.mainloop()