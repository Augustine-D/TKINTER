import tkinter as tk

root = tk.Tk()

l = tk.Label(root, text='Input box').pack()

e = tk.Entry(root, width=50)
e.pack()
# default text inside text box
e.insert(0, 'Enter your name')


def myClick():
    myLabel = tk.Label(root, text="Hello " + e.get())
    myLabel.pack()


myButton = tk.Button(root, text='Enter Your Name', command=myClick)
myButton.pack()

root.mainloop()
