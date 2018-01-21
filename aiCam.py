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

   # IBM Watson post
   url   = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key='YOUR-WATSON-API-KEY-HERE'&version=2016-05-20'
   files = {'images_file': open('/home/pi/Desktop/motionCam/images/image.png','rb')}
   req   = requests.post(url, files=files)

   data = req.json()

   # workaround for Python returning the JSON object as a dictionary that is very hard to work with.
   # find() function returns -1 if the string is not matched. Index of string if it is matched.
   # the string to find variable is the classification that IBM Watson gives to a person or a group of people.
   # If you want to look for something other than a person, change the stringToFind variable, but check out the -
   # IBM Watson response object to see the types of classification strings that are used, so that you know what to look for. 
   stringToFind = 'person'

   if str(data).find(stringToFind) > -1:
      message = client.messages.create(
        to    = "PHONE-YOU-WANT-TO-REACH",
        from_ = "YOUR-TWILIO-NUMBER",
        body  = "Someone tripped the alarm")

   
   



