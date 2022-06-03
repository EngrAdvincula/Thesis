#Intro GUI for Temperature Scanner. Proceed Button is placed here for Temp Scanning

from tkinter import *
import tryQrOnly as tqr
from time import sleep as slp
import idleWindow as iw


def tryQRF():
    theme='#4d97fe'

    def tryQROne():
        slp(2)
        window.destroy()
        tqr.checkQrCode()
        iw.loopingWindow()
        
          
    window = Tk()
    window.config(cursor="none")
    window.title("IOT")
    window.geometry('700x480')
    window.configure(bg='white')
    window.overrideredirect(1)
    lbl=Label(window,text="Please Scan your QR Code", fg='black', bg='white')
    lst=('Calibri (Body)', 28, 'bold')
    lbl.config(font=lst)
    lbl.place(x=45,y=160)
    buttn = Button(window, width=7, height=2, text="SCAN QR", fg='white', border=0, command=tryQROne, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=260,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    
    window.mainloop()
    
