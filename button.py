#import tkinter
import tkinter as tk

# setting root window
root = tk.Tk()


def mylabel():
    label_1 = tk.Label(root, text='Augustine').pack()


# creating label
mybutton = tk.Button(root, text='\n Click Me \n', padx=50,
                     pady=50, command=mylabel).pack()

# main loop of the program
root.mainloop()
