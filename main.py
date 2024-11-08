import RPi.GPIO as GPIO
import time
import requests
import json
import time
import datetime

GPIO.setmode(GPIO.BCM) 
MOTION_PIN = 14 
GPIO.setup(MOTION_PIN, GPIO.IN)

def detect_motion():
    if GPIO.input(MOTION_PIN):
        print("Motion Detected")
        return True
    print("No Motion Detected")    
    return False


def send_notification(message):
    data_send = {"type": "note", "body": message}
    requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data=json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + '<PushBullet API Key>',
                     'Content-Type': 'application/json'})


MOTION_THRESHOLD = 10  
MOTION_TIMEOUT = 5 * 60 

last_motion_time = time.time() 
motion_count = 0 
washer_dryer_on = False

while True:
    current_time = time.time()    
    motion_detected = detect_motion()
        
    if motion_detected:
        motion_count += 1 
        last_motion_time = current_time  
    
    if motion_count >= MOTION_THRESHOLD and not washer_dryer_on:
        washer_dryer_on = True
        send_notification("Washer and Dryer started. Monitoring...")
    
    if current_time - last_motion_time >= MOTION_TIMEOUT and washer_dryer_on:
        send_notification("No motion detected for 5 minutes. Washer and Dryer are likely off.")
        washer_dryer_on = False
    
    time.sleep(1)

