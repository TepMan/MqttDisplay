# !/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from display import display_init, display_message, display_cleanup
import paho.mqtt.client as mqtt


# def on_message(client, userdata, message):
#
#     payload = str(message.payload.decode("utf-8"))
#
#     logging.info("message received ", payload)
#     logging.info("message topic=", message.topic)
#     logging.info("message qos=", message.qos)
#     logging.info("message retain flag=", message.retain)


# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

try:
    # logging.info("MQTT Client start")
    #
    # client = mqtt.Client("status-pi")
    # client.connect("raspi4")
    # client.subscribe("iob")
    # client.on_message = on_message
    #
    # logging.info("MQTT Client created, starting message loop")
    #
    # client.loop_start()  # start the loop
    #
    # time.sleep(10)
    #
    # logging.info("stopping messwage loop")
    # client.loop_stop()  # stop the loop
    #
    # logging.info("exit program")

    display_init()
    logging.info("Display init completed")

    while True:
        # display_message('AAAAAAA')
        # display_message('   AAAAA   ')
        display_message(time.strftime('%H:%M') + ' Uhr')
        time.sleep(10)
        display_message(time.strftime('%d.%m.%Y'))
        time.sleep(10)


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    display_cleanup()
    logging.info("Display cleanup completed")
    logging.info("Program end")
    # client.loop_stop()
    exit()
