from picamera import PiCamera
from gpiozero import MotionSensor
from os.path import join, dirname
from os import environ
from twilio.rest import Client
import requests
import json

#MotionSensor parameter is a delay timer
pir    = MotionSensor(4)
camera = PiCamera()

# Your Account SID From twilio.com/console
account_sid = "YOUR-TWILIO-ACCOUNT-SID"

# Your Auth Token from twilio.com/console
auth_token = "YOUR-TWILIO-AUTH-TOKEN-HERE"

client = Client(account_sid, auth_token)

# Use this if you want to have the sensor always running
#while True:
#   pir.wait_for_motion()

if pir.wait_for_motion() == True: 
   camera.capture('/home/pi/Desktop/motionCam/images/image.png')
   camera.close()
   print("Movement")

   #IBM Watson post
   url   = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key='YOUR-WATSON-API-KEY-HERE'&version=2016-05-20'
   files = {'images_file': open('/home/pi/Desktop/motionCam/images/image.png','rb')}
   req   = requests.post(url, files=files)

   data = req.json()

   #workaround for Python returning the JSON object as a dictionary that is very hard to work with.
   str2 = 'person'

   if str(data).find(str2) > -1:
      message = client.messages.create(
        to    = "PHONE-YOU-WANT-TO-REACH",
        from_ = "YOUR-TWILIO-NUMBER",
        body  = "Someone tripped the alarm")

   
   



