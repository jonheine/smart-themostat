#!/bin/env python3

import sys
import time
import paho.mqtt.client as mqtt #import the client1


def settemp(temp):

    broker_address="localhost" 
    #broker_address="iot.eclipse.org"
    print("creating new instance")
    client = mqtt.Client("SThermClient") #create new instance
    print("connecting to broker")
    client.connect(broker_address) #connect to broker
    #print("Subscribing to topic","house/bulbs/bulb1")
    #client.subscribe("house/bulbs/bulb1")
    client.publish("house/thermostat/setpoint","%.2f" % temp)



if __name__ == '__main__':

    temp = 21.0
    settemp(temp)

    for arg in sys.argv[1:]:
        settemp(float(arg))
        time.sleep(3)

