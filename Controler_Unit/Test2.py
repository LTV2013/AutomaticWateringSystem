import RPi.GPIO as GPIO
import time
import mysql.connector
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import schedule
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)
# chan = AnalogIn(ads, ADS.P0)

GPIO.setmode(GPIO.BCM)

mydb = mysql.connector.connect(
    host="192.168.178.23",
    user="admin",
    password="root",
    database="Plants"
    )

cursor = mydb.cursor()

# As GPIO
pumpsAndSensors=[{"GPIO_PIN": 27,
                  "Channel": AnalogIn(ads, ADS.P0),
                  "PlantName": "Rose"},
                 {"GPIO_PIN": 17,
                  "Channel": AnalogIn(ads, ADS.P1),
                  "PlantName": "Sunflower"}]

for entry in pumpsAndSensors:
    GPIO.setup(entry["GPIO_PIN"], GPIO.OUT)

def update_chan_value(channel):
    return channel.value

def water():
    for entry in pumpsAndSensors:        
        currentChanValue = update_chan_value(entry["Channel"])
        print(currentChanValue)
        if currentChanValue < 22000:
            GPIO.output(entry["GPIO_PIN"], GPIO.LOW)
            time.sleep(5)
            GPIO.output(entry["GPIO_PIN"], GPIO.HIGH)
            print("Watered")
            
        update_db(currentChanValue, entry["PlantName"])
        
def update_db(aChanValue, aPlantName):
    
    try:
        queryString = "UPDATE classroom SET moisture_lvl = " + str(aChanValue) + " WHERE plant_name = '" + aPlantName + "'"
        print(queryString)
        cursor.execute(queryString)
        mydb.commit()
        print("Successfully saved to database")
    except:
        print("An Error occured while trying to save to database")
    
def main():
    water()

schedule.every(3).seconds.do(water)
main()
while True:
    schedule.run_pending()
GPIO.cleanup()
