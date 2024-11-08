import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM) 
MOTION_PIN = 14 
GPIO.setup(MOTION_PIN, GPIO.IN)

TIME_LIMIT = 300
last_motion_time = time.time()

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
            print("Alert: It seems like th washer and dryer have stopped!")    
            break

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup() 
