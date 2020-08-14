#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description : read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
DHTPin = 11     #define the pin of DHT11
TempThreshold = 24
TempMin = 20
dht = DHT.DHT(DHTPin)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FanPin = 21
GPIO.setup(FAN_PIN, GPIO.OUT)

while True:
    time.sleep(1)
    #Read the Temp Sensor
    chk = dht.readDHT11()
    if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print("DHT11,OK!")
    print("Temp: %.2f "%(dht.temperature))
    
    #Control the fan based on the Temp
    if(dht.temperature > TempThreshhold):
        GPIO.output(FanPin, True)
    if(dht.temperature < TempMin):
        GPIO.output(FanPin, False)
    