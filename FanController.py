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
TempThreshold = 22.0
TempMin = 20.0
dht = DHT.DHT(DHTPin)

GPIO.setwarnings(False)
FanPin = 40
GPIO.setup(FanPin, GPIO.OUT)

while True:
    time.sleep(10)
    #Read the Temp Sensor
    chk = dht.readDHT11()
    if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print("DHT11,OK!")
    print("Temp: %.2f "%(dht.temperature))
    
    #Control the fan based on the Temp
    if(dht.temperature > TempThreshold):
        GPIO.output(FanPin, True)
    if(dht.temperature < TempMin):
        GPIO.output(FanPin, False)
    
