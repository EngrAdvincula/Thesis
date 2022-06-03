#Intro GUI for Temperature Scanner. Proceed Button is placed here for Temp Scanning

from tkinter import *
from time import sleep as slp
import idleWindow as iw
import cv2
import main as m

def QRGUIFinalAccess():
    cv2.destroyAllWindows()
    theme='#4d97fe'

    def proceed():
        window.destroy()

    window = Tk()
    window.config(cursor="none")
    window.title("QR Code Results")
    window.geometry('700x480')
    window.configure(bg='white')
    window.overrideredirect(1)
    lbl=Label(window,text="QR Code Accepted", fg='black', bg='white')
    lst=('Calibri (Body)', 28, 'bold')
    lbl.config(font=lst)
    lbl.place(x=140,y=160)
    buttn = Button(window, width=15, height=2, text="Open the Lock", fg='white', border=0, command=proceed, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=200,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    window.mainloop()
    
def QRGUIFinalDenied():
    cv2.destroyAllWindows()
    theme='#4d97fe'

    def proceed():
        window.destroy()
        iw.loopingWindow()
        cv2.destroyAllWindows()

    window = Tk()
    window.title("QR Code Results")
    window.geometry('800x480')
    window.configure(bg='white')
    window.overrideredirect(1)
    lbl=Label(window,text="QR Code Denied", fg='black', bg='white')
    lst=('Calibri (Body)', 28, 'bold')
    lbl.config(font=lst)
    lbl.place(x=140,y=160)
    buttn = Button(window, width=7, height=2, text="Thanks", fg='white', border=0, command=proceed, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=260,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    window.mainloop()

def QRGUIError():
    cv2.destroyAllWindows()
    theme='#4d97fe'

    def proceed():
        window.destroy()
        cv2.destroyAllWindows()
        quit()

    window = Tk()
    window.title("QR Code Results")
    window.geometry('800x480')
    window.configure(bg='white')
    window.overrideredirect(1)
    lbl=Label(window,text="Unexpected Error", fg='black', bg='white')
    lst=('Calibri (Body)', 28, 'bold')
    lbl.config(font=lst)
    lbl.place(x=140,y=160)
    buttn = Button(window, width=7, height=2, text="Try Again", fg='white', border=0, command=proceed, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=260,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    window.mainloop()
