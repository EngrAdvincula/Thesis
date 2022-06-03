from tkinter import *
import systemProcesses as sp
import SystemDataBase as db
import cv2
import requests

def errorWindow():

    theme='#4d97fe'
    

    def proceedWindow():
        windows.destroy()
        cv2.destroyAllWindows()
        
    
    windows = Tk()
    windows.title("IOT")
    windows.geometry('700x480')
    windows.configure(bg='white')
    windows.overrideredirect(1)
    lbl=Label(windows,text="Unexpected Error, Please Try Again", fg='black', bg='white')
    lst=('Calibri (Body)', 28, 'bold')
    lbl.config(font=lst)
    lbl.place(x=190,y=160)
    buttn = Button(windows, width=7, height=2, text="PROCEED", fg='white', border=0, command=proceedWindow, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=190,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    windows.mainloop()


