import cv2
import SystemDataBase as db
import QRGUI as qrg
import RPi.GPIO as GPIO
from time import sleep as slp
import SystemDataBase as sdb

solenoidPin = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoidPin, GPIO.OUT)

def checkQrCode():
    try:
        # set up camera object
        cap = cv2.VideoCapture(-1)
        # QR code detection object
        detector = cv2.QRCodeDetector()

        i = 0
        while True:
            # get the image
            _, img = cap.read()
            # get bounding box coords and data
            data, bbox, _ = detector.detectAndDecode(img)

            if data:
                if data == db.todaysQRData[i]:
                    qrg.QRGUIFinalAccess()
                    slp(2)
                    GPIO.output(solenoidPin, GPIO.LOW)
                    slp(10)
                    GPIO.output(solenoidPin, GPIO.HIGH)
                    sdb.entryQrCodeData.append(data)
                    print("QR Code is Accepted")
                    return [True, data]
                    break
                elif len(db.todaysQRData)-1 == i:
                    qrg.QRGUIFinalDenied()
                    print("QR Code Not Allowed")
                    return [False, data]
                    break
                else:
                    i = i+1
                    
            

            # display the image preview
            #cv2.imshow("code detector", img)
            if(cv2.waitKey(1) == ord("q")):
                break
        
        # free camera object and exit
        cap.release()
        cv2.destroyAllWindows()
    
    except:
        qrg.QRGUIError()
    
    
    







