# Thesis

import cv2
import RPi.GPIO as GPIO
import time
from time import sleep
import board
import busio as io
import adafruit_mlx90614


#If code is stopped while the solenoid is active it stays active
#This may produce a warning if the code is restarted and it finds the GPIO Pin, which it defines as non-active in next line, is still active
#from previous time the code was run. This line prevents that warning syntax popping up which if it did would stop the code running.
GPIO.setwarnings(False)
#This means we will refer to the GPIO pins
#by the number directly after the word GPIO. A good Pin Out Resource can be found here https://pinout.xyz/
GPIO.setmode(GPIO.BCM)
#This sets up the GPIO 18 pin as an output pin
GPIO.setup(24, GPIO.OUT)

cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

#For Infrared Temperature Scanner
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)



print("Please scan your Temperature, Please place your hands near the Sensor")

tTemp = 36.76
#while True:
    #ambientTemp = round((float("{:.2f}".format(mlx.ambient_temperature))+3),2)
    #targetTemp = round((float("{:.2f}".format(mlx.object_temperature))+3),2)
    #if (targetTemp >= (ambientTemp+1)):
        #tTemp = targetTemp
        #break
       
#sleep(3)
#print("Your Temperature is: " + str(tTemp))
sleep(3)
print("Please scan your QR Code")

#Keeps the program looping until it breaks
while True:

    #Data to be assessed if Allowed or not
    keys = ["www.wikipedia.com", "helloworld", "HiMark", "JillPogi"]

    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a = data
        for i in range(len(keys)):
                if ((keys[i] == a) and (tTemp < 37)):
                    #here lies solenoid access and LED light
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setwarnings(False)
                    GPIO.output(24, 0)
                    GPIO.setup(23,GPIO.OUT)
                    GPIO.output(23,GPIO.HIGH)
                    time.sleep(5)
                    GPIO.output(23,GPIO.LOW)
                    print("Access Granted")
                    break
                else:
                    # here lies solenoid non-access and LED light
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setwarnings(False)
                    GPIO.output(24, 1)
                    GPIO.setup(18,GPIO.OUT)
                    GPIO.output(18,GPIO.HIGH)
                    time.sleep(5)
                    GPIO.output(18,GPIO.LOW)
                    print("Access Denied")
                    break
        break

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
