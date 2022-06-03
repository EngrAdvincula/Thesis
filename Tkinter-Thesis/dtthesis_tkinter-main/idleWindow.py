from tkinter import *
import systemProcesses as sp
import SystemDataBase as db
import cv2
import requests

def loopingWindow():

    cv2.destroyAllWindows()
    theme='#4d97fe'
    

    def proceedWindow():
        windows.destroy()
        if (db.accessData == 'QRandTemp'):
            sp.goQRandTemp()
        elif (db.accessData == 'QROnly'):
            sp.goQROnly()
        elif (db.accessData == 'TempOnly'):
            sp.goTempOnly()
    
    def closeWindow():
        windows.destroy()
        if(len(db.entryQrCodeData) == 0):
            x = requests.post("http://dt-iotdoorlock.online/api/entries", data = {'date':db.dateToday, 'QRentries':"No Content", 'TempEntries':",".join(db.entryTempData)})
            print(x.text)
        elif(len(db.entryTempData) == 0):
            y = requests.post("http://dt-iotdoorlock.online/api/entries", data = {'date':db.dateToday, 'QRentries':",".join(db.entryQrCodeData), 'TempEntries':"No Content"})
            print(y.text)
        else:
            z = requests.post("http://dt-iotdoorlock.online/api/entries", data = {'date':db.dateToday, 'QRentries':",".join(db.entryQrCodeData), 'TempEntries':",".join(db.entryTempData)})
            print(z.text)
        
        
        
    windows = Tk()
    windows.config(cursor="none")
    windows.title("IOT")
    windows.geometry('700x480')
    windows.configure(bg='white')
    windows.overrideredirect(1)
    lbl=Label(windows,text="Let's Proceed", fg='black', bg='white')
    lst=('Calibri (Body)', 28, 'bold')
    lbl.config(font=lst)
    lbl.place(x=190,y=160)
    buttn = Button(windows, width=7, height=2, text="PROCEED", fg='white', border=0, command=proceedWindow, bg=theme,  activebackground=theme, activeforeground='white')
    buttn.place(x=190,y=250)
    lg=('Calibri (Body)',16, 'bold')
    buttn.config(font=lg)
    buttn2 = Button(windows, width=7, height=2, text="CLOSE", fg='white', border=0, command=closeWindow, bg='red',  activebackground='red', activeforeground='white')
    buttn2.place(x=350,y=250)
    buttn2.config(font=lg)
    