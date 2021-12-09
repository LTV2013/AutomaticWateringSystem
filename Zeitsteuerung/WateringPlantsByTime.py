import RPi.GPIO as GPIO
import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import schedule
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

GPIO.setmode(GPIO.BCM)


pumps=[5, 6, 13, 19]

def setup():
    for i in pumps:
        GPIO.setup(i, GPIO.OUT)

def water():
    print(chan.value)
    if chan.value < 20000:
        for i in pumps:
            GPIO.output (i, GPIO.LOW)
            time.sleep(5)
            GPIO.output (i, GPIO.HIGH)
            print("Watered")

def main():
    setup()
    water()
    

schedule.every(10).seconds.do(water)
main()
while True:
    schedule.run_pending()
GPIO.cleanup()
