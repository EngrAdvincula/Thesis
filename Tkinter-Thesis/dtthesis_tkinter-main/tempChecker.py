from tkinter import *
import board
import busio as io
import adafruit_mlx90614
from time import sleep as slp
import RPi.GPIO as GPIO
import SystemDataBase as sdb
import TryTemp as tp

solenoidPin = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoidPin, GPIO.OUT)

def tempTsek():
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)
    
    window = Tk()
    window.config(cursor="none")
    window.title("IOT")
    window.geometry('700x480')
    window.configure(bg='white')
    window.overrideredirect(1)
    
    def proceed():
        window.destroy()
        slp(2)
        GPIO.output(solenoidPin, GPIO.LOW)
        slp(10)
        GPIO.output(solenoidPin, GPIO.HIGH)
    
    def tryTempAgain():
        window.destroy()
        tp.tryTempGUI()
    
    while True:
        ambientTemp = round((float("{:.2f}".format(mlx.ambient_temperature))),2)
        targetTemp = round((float("{:.2f}".format(mlx.object_temperature))+1.5),2)
        #print (str(targetTemp) + " " + str(ambientTemp))
        if(targetTemp < 37.5):
            sdb.entryTempData.append(str(targetTemp))
            print(sdb.entryTempData)
            print(",".join(sdb.entryTempData))
            theme='#4d97fe'
            lbl=Label(window,text="Normal Temperature: " + str(targetTemp), fg='black', bg='white')
            lst=('Calibri (Body)', 27, 'bold')
            lbl.config(font=lst)
            lbl.place(x=35,y=160)
            buttn = Button(window, width=15, height=2, text="Open the Lock", fg='white', border=0, command=proceed, bg=theme,  activebackground=theme, activeforeground='white')
            buttn.place(x=200,y=250)
            lg=('Calibri (Body)',16, 'bold')
            buttn.config(font=lg)
            window.mainloop()
            
            break
        else:
            theme='#4d97fe'
            lbl2=Label(window,text="High Temperature Detected: " + str(targetTemp), fg='black', bg='white')
            lst2=('Calibri (Body)', 23, 'bold')
            lbl2.config(font=lst2)
            lbl2.place(x=28,y=160)
            buttn = Button(window, width=15, height=2, text="Try Again", fg='white', border=0, command=tryTempAgain, bg=theme,  activebackground=theme, activeforeground='white')
            buttn.place(x=200,y=250)
            lg=('Calibri (Body)',16, 'bold')
            buttn.config(font=lg)
            window.mainloop()
            break

    