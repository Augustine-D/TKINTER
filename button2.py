#import tkinter
import tkinter as tk

# setting root window
root = tk.Tk()


def mylabel():
    label_1 = tk.Label(root, text='Augustine').pack()


# creating label
mybutton = tk.Button(root, text='\n Click Me \n', padx=10,
                     pady=10, command=mylabel, fg='red', background='yellow').pack()

# main loop of the program
root.mainloop()
