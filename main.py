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
def msg():
    a1 = e1.get()
    m1 = "Hey " + a1 + "\n Welcome to my window"
    l3 = Label(root, text=m1)
    l3.pack()

b1 = Button(root, text="Submit", bg="red", fg="white", command=msg)
b1.pack()

root.mainloop()



