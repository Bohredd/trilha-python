import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open("https://www.google.com")

mygoogle = Button(root, text="Abrir Google!",command=google)
mygoogle.pack(pady=20)

root.mainloop()
