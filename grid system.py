#import tkinter
import tkinter as tk

# setting root window
root = tk.Tk()

# creating label
myLabel = tk.Label(root, text='Hello Augustine, ')
myLabel_2 = tk.Label(root, text=' ')
myLabel_3 = tk.Label(root, text='   ')
myLabel_1 = tk.Label(root, text=' How are you doing')

# displaying on screen
myLabel.grid(row=0, column=0)
myLabel_2.grid(row=2, column=0)
myLabel_3.grid(row=3, column=0)
myLabel_1.grid(row=4, column=0)

# main loop of the program
root.mainloop()
