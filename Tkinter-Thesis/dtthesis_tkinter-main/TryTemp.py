#Intro GUI for Temperature Scanner. Proceed Button is placed here for Temp Scanning

from tkinter import *
import tempChecker as tpp
from time import sleep as slp
import idleWindow as iw
import cv2

def tryTempGUI():
    cv2.destroyAllWindows()
    
    theme='#4d97fe'

    def tryTempGUIOne():
        slp(4)
        window.destroy()
        tpp.tempTsek()
        iw.loopingWindow()
          
    window = Tk()
    window.config(cursor="none")
    window.title("IOT")
    window.geometry('700x480')
    window.configure(bg='white')
    window.overrideredirect(1)
    lbl=Label(window,text="Please Scan your Temperature", fg='black', bg='white')
    lst=('Calibri (Body)', 25, 'bold')
    lbl.config(font=lst)
    lbl.place(x=30,y=160)
    buttn = Button(window, width=9, height=2, text="SCAN Temp", fg='white', border=0, command=tryTempGUIOne, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=260,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    
    window.mainloop()
    