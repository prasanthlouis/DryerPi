import RPi.GPIO as GPIO
import time
import requests
import json

GPIO.setmode(GPIO.BCM) 
MOTION_PIN = 14 
GPIO.setup(MOTION_PIN, GPIO.IN)

TIME_LIMIT = 300
last_motion_time = time.time()



data_send = {"type": "note", "body": "Program is starting"}
requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data=json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + '<Bearertoken>',
                     'Content-Type': 'application/json'})
try:
    print("Motion Detection Started...")
    while True:
        if GPIO.input(MOTION_PIN):
            print("Motion Detected!")
            last_motion_time = time.time()
            time.sleep(1)  
        else:
            print("No Motion.")
        time.sleep(0.5)  

        if time.time() - last_motion_time > TIME_LIMIT:
            data_send = {"type": "note", "body": "Dryer + Washer has stopped!"}
            requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data=json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + '<Bearer token',
                     'Content-Type': 'application/json'})
            break

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup() 
