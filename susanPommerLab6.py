###########################################################
# Course:  CS21B Python Programming: Lab #6
# Name:  Susan Pommer
#
# Description:  This program launches a GUI which asks a user
# to enter to a distance in kilometers into a text box, then
# on click of a 'Convert' button, calculates the distance in
# miles and displays the results in an information dialogue box.
# User also has the option to click 'Quit' button to end.

# File name:  susanPommerLab6.py
# Date:  February 27, 2018
###########################################################

# Import tkinter GUI library and widgets
import tkinter

# Import required tkinter widgets
from tkinter import Tk, Label, Button, Entry, END, Text
from tkinter import Frame

# Import tkinter message box
from tkinter.messagebox import showinfo

## ------- DEFINE CLASS -------------------------#

class ButtonClick(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=100, height=100)

        # Add single-line text entry box to window
        self.kilos_entered = Entry(self, width=15)
        self.kilos_entered.grid(row=2,column=1, \
                        columnspan=2, pady=5)

        # Create button labeled 'Convert'
        # with event handler click_convert
        button_convert = Button(self, text='Convert', \
                        bg='green', fg='white', padx=5,\
                        command=self.click_convert)
        button_convert.grid(row=3, column=1)

        # Create button labeled 'Quit'
        # with event handler click_quit
        button_quit = Button(self, text='Quit', \
                        bg='red', fg='white', padx=10, \
                        command=self.click_quit)
        button_quit.grid(row=3, column=2)

    # On click of 'Convert' button, calculate and display miles
    def click_convert(self):
        # Return string in entry kilos_entered
        kilometers = self.kilos_entered.get()
        # Convert input to floating variable for calcs
        kilos_float = float(kilometers)

        # Calculate conversion to miles
        miles = (kilos_float * 0.6214)

        # Create calculated miles output statement
        miles_statement = ("%10.2f kilometers are equivalent to: "\
                        "\n%10.2f miles" % (kilos_float, miles))

        # Display output statement in information text box
        showinfo(message=miles_statement)

        # Delete entry to prepare for next user entry in
        self.kilos_entered.delete(0, END)

    # On click of 'Quit' button, exit program
    def click_quit(self):
        exit(0)


## --------------BUILD AND LAUNCH GUI ------------------------###

# Create top-level root window GUI object
root = tkinter.Tk()

# Set minimum size for the master window
root.minsize(200,120)

# Add and style a label for root window
label_header = Label(root, \
            text='Kilometers to Miles Converter', \
            font=('', 12, 'bold'), )
label_header.grid(row=0, column=0, columnspan=2)

# Create label for user data entry box
label_entry = Label(root, text='Enter distance in kilometers:')
label_entry.grid(row=1, column=0)

# Call the Button Click Class
click_action = ButtonClick(root)
click_action.grid()

# Start the GUI
root.mainloop()

## -------------------- SAMPLE RUN --------------------------- ##
#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab6.py"

#Process finished with exit code 0

# Also see:  Lab_6_Screen_Capture_022518.jpeg

## -------------------------------------------------------------##
