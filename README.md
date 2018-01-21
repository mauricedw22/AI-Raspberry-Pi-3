# AI-Raspberry-Pi-3
Easily turn your Raspberry pi into an AI camera. 

This project uses a motion sensor to detect movement, once movement is detected a photograph is taken and saved to a folder. This photograph is saved as a .png, the .png file is sent to IBM Watson for classification. The response is parsed, in the case of this particular project if the .png contains a "Person" classification, meaning if a picture of a person was taken, the applicaton will use the Twilio SMS service and send an SMS message to a number of your choosing. If the .png is not classified as a person no SMS message will be sent. Viola, you have a low cost AI camera build by you in a short amount of time.  

Hardware required to reproduce this project.
1. Raspberry Pi 3.
2. Raspberry Pi camera module.
3. Passive Infrared Sensor (PIR).
4. Three female to female jumper wires.

Software required to reproduce this project.
1. Python 2.7 
2. PIP - Python Package Index
3. Twilio Python SDK found here ---> https://www.twilio.com/docs/libraries/python
4. If you follow the instructions given by Twilio the SDK will not install, simply use ---> sudo pip install twilio
5. Take note of comments in code that tell you to put in your credentials for the required Twilio credentials. Your credentials can be found in the console section of Twilio services.
6. You will need to purchase a Twilio phone number which is priced at ~1 dollar per month.
7. You will need to sign up for the Twilio SMS service. The fee is a per message fee. Check with Twilio.com/sms for fee info.
8. You will need to look in the code to see where the sender number is located and replace it with your Twilio number.
9. You will need an IBM Watson account. Click on get started free ---> https://www.ibm.com/watson/services/visual-recognition/
10. Set up an account with IBM Watson. 
11. Take note of your IBM Watson API KEY, when noted in code please place your API KEY.

Motion sensor setup
1. Set up the 5 volt, ground, and digital input female to female jumper wires according to this diagram --> 
https://projects-static.raspberrypi.org/projects/rpi-gpio-connect-pir/f486753f7a342f6f379ea947b695541d5c793396/en/images/pir-diagram.png

Getting up an running
1. Install pip on the Raspberry Pi if you don't already have it installed. 
2. Use sudo apt-get update to first update.
3. Use sudo apt-get install python-pip
4. sudo pip install twilio
5. Create this file structure ---> /home/pi/Desktop/motionCam/images so that you can store the .png that is taken.  
6. This is everything that you need to run this project. If you run into compatibility issues with the code simply install or update the packages that Python complains about.
