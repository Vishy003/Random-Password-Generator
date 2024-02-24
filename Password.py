from tkinter import Tk, Entry, Button, LabelFrame, Frame, messagebox
import tkinter as tk  # Import tkinter module
from random import randint


root = Tk()
root.title('Random Password Generator')
root.geometry("500x300")

# Generate Random Strong Password
def new_rand():
    # Clearing our Entry Box
    pw_entry.delete(0, tk.END)

    # Getting the PW Length and converting it to Integer
    pw_length = int(my_entry.get())

    # Creating a variable to hold our Password
    my_password = ''

    # Looping through Password Length
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    # Output Password to the Screen
    pw_entry.insert(0, my_password)
    
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Random Password Generator","Password Successfully Copied to Clipboard!")

# Label Frame
lf = LabelFrame(root, text = "How Many Characters?")
lf.pack(pady = 20)

# Creating Entry Box To Designate the Number of Characters
my_entry = Entry(lf, font = ("Helvetica", 24))
my_entry.pack(pady = 20, padx = 20)

# Creating an Entry Box for our Returned Password
pw_entry = Entry(root, text = '', font = ("Helvetica", 24), bd = 0, bg = "systembuttonface")
pw_entry.pack(pady = 20)

# Creating a Frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady = 20)

#Creating our Buttons
my_button = Button(my_frame, text = "Generate Strong Password", command = new_rand)
my_button.grid(row = 0, column = 0, padx = 10)

clip_button = Button(my_frame, text = "Copy To Clipboard", command = clipper)
clip_button.grid(row = 0, column = 1, padx = 10)

root.mainloop()
