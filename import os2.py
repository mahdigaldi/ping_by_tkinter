
import time
import os
from tkinter import *
from ping3 import ping


hostname = "google.com" #example

def chek():
    global response
    #while True:
    response = ping(hostname)

def pan():
    win=Tk()
    win.title("router")
    win.geometry("500x400")


    base_frame=Frame(win,width=500,height=400)
    base_frame.pack()

#base_frame.place(anchor="center",relx=0.5,rely=0.5)

    global Label_server
    Label_server=Label(base_frame,text="server is on ")
    Label_server.pack()
    mainloop()



def chek2(response):
    if response==False:
        Label_server.config(text="server is of",font="tahoma 16 ",bg="red")    
    else:
        pass




while True:
    pan()
    chek()
    chek2(response)

    





