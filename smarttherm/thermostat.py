#!/bin/env python3

import sys
import time
import paho.mqtt.client as mqtt #import the client1


class Thermostat:

    def __init__(self, broker):
        self.client = mqtt.Client("STherm") 
        self.client.connect(broker)

        self.client.on_message = lambda c, ud, msg : self.on_message(c, ud, msg)
        self.client.subscribe("house/thermostat/getstate")
        self.client.subscribe("house/thermostat/setpoint")
        self.client.loop_start();


    def __del__(self):
        self.client.loop_stop();

    def on_message(self, client, userdata, message):
        func = message.topic[17:] # remove house/thermostat/
        getattr(self, func)(str(message.payload.decode('utf-8')))

    def getstate(self, payload):
        print("getstate %s\n" % (payload))

    def setpoint(self, payload):
        print("setpoint %s\n" % (payload))


    def run(self):

        self.running = True
        while(self.running):
            time.sleep(10)
            print ('sending status')


if __name__ == '__main__':

    therm = Thermostat('localhost')
    therm.run()

