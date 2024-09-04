#to create a windows
# from tkinter import*
# root=Tk ()
# root.mainloop()

#to add title
# from tkinter import*
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('130x200')
# root.mainloop()


#placing lable
# from tkinter import *
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('130x200')
# l1=Label(root,text="we are python lobbi-ian")
# l1.pack()
# root.mainloop()



#to create a button
# from tkinter import *
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('700x200')
# l1=Label(root,text="To register")
# l1.pack()
# def clicked():
#     print("I am clicked")
# btn=Button(root,text="click",command=clicked)
# btn.pack()
# #root.geometry("700x200")
# root.mainloop()

#to enter anything

#to add title
# from tkinter import*
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('130x200')
# root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
label = Label(root, text="This is Image").pack(side=TOP, pady=10)

path = PhotoImage(file="C:/Users/HP/Pictures/flower.png")
label_image = Label(root, image=path,width=400, height=400)
label_image.pack()

root.geometry("600x440")
root.title("PythonLobby.com")
root.mainloop()