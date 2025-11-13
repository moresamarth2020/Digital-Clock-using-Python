import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')  # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1 second

# Create the main window
root = tk.Tk()
root.title("🕒 Digital Clock")

# Styling the clock label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Call time() function
time()

# Run the clock
root.mainloop()
