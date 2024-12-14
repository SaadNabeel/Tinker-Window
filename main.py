from tkinter import *

root = Tk()
root.title('My window')
root.geometry('300x300')
root.config(background="yellow")

l1 = Label(root, text="Registration Form", bg="light blue", fg="red", font=('Arial', 29), padx=10, pady=10)
l1.pack()

l2 = Label(root, text="Enter your name", bg="light green", fg="red", font=('Arial', 29), padx=10, pady=10)
l2.pack()

e1 = Entry(root)
e1.pack()

b1 = Button(root, text="Submit", bg="red", fg="white")
b1.pack()

root.mainloop()


