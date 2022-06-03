import qrCodeDetector as qrd 
from time import sleep as slp
from tkinter import *
import TryTemp as tTemp
import RPi.GPIO as GPIO
import tryQR as tq
import tryQR2 as tq2

solenoidPin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoidPin, GPIO.OUT)
GPIO.output(solenoidPin, GPIO.HIGH)

def goQRandTemp():
    tq2.tryQRF2()

def goQROnly():
    tq.tryQRF()
    
        
def goTempOnly():
    tTemp.tryTempGUI()


    
        
        
    

# if __name__ == "__main__":
#     main()