import socket
from tkinter import *
import pyperclip


def generateIP():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ipgen.set(ip_address)


def copyIP():
    ip_copy = ipgen.get()
    pyperclip.copy(ip_copy)


top = Tk()
top.geometry("400x200")
top.title("IP generator")
ipgen = StringVar()
Label(top, text="IP generator", font="calibiri 20 bold").pack()
Button(top, text="Generate your IP", command=generateIP).pack(pady=7)
Button(top, text="Copy IP Address", command=copyIP).pack(pady=7)
Entry(top, textvariable=ipgen).pack(pady=3)
top.mainloop()
