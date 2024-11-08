import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM) 
MOTION_PIN = 14 
GPIO.setup(MOTION_PIN, GPIO.IN)

try:
    print("Motion Detection Started...")
    while True:
        if GPIO.input(MOTION_PIN):
            print("Motion Detected!")
            time.sleep(1)  
        else:
            print("No Motion.")
        time.sleep(0.5)  

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup() 
