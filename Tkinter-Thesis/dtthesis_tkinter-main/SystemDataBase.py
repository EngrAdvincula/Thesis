import requests
from datetime import date

dateToday = str(date.today())
QRData = requests.get("http://dt-iotdoorlock.online/site/jsondata?filter[appointmentStart]=" + dateToday)
#QRData = requests.get("http://dt-iotdoorlock.online")
AccessData = requests.get("http://dt-iotdoorlock.online/api/access")

QRDataJson = QRData.json()
AccessDataJson = AccessData.json()


todaysQRData = []
entryQrCodeData = []
entryTempData = []
accessData = ''


for i in QRDataJson:
    todaysQRData.append(i['qrCode'])

for i in AccessDataJson:
    if (AccessDataJson[0]['QRandTemp'] == "True"):
        accessData = 'QRandTemp'
    elif (AccessDataJson[0]['QROnly'] == "True"):
        accessData = 'QROnly'
    elif (AccessDataJson[0]['TempOnly'] == "True"):
        accessData = 'TempOnly'

#print(todaysQRData)
#print(entryQrCodeData)
#print(entryTempData)
#print(accessData)
#print(entryTempData)
#print(forUploadTemp)








