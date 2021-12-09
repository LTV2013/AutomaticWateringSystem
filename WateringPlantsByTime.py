import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)


GPIO.output (4, GPIO.LOW)
GPIO.output (3, GPIO.HIGH)
print("test")
time.sleep(3)
print("test")
GPIO.output (4, GPIO.HIGH)
GPIO.output (3, GPIO.LOW)
time.sleep(3)


GPIO.cleanup()