# !/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from display import display_init, display_message, display_cleanup
import paho.mqtt.client as mqtt
from queue import Queue

# MessageQueue anlegen
mq = Queue()

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)


def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    mq.put(payload)
    logging.info("Message = " + payload)


def on_log(client, userdata, level, buf):
    logging.info("Log: " + buf)


try:
    display_init()
    logging.info("Display init completed")

    client = mqtt.Client("StatusPI")
    client.on_message = on_message
    client.on_log = on_log
    logging.info("MQTT Client started")

    client.connect(host="raspi4", port=1883, keepalive=60)
    logging.info("Client connected")

    client.subscribe("iob/#")
    logging.info("Client subscribed")

    client.loop_start()
    logging.info("Client loop startes")

    while True:
        while not mq.empty():
            message = mq.get()
            if message is None:
                continue
            display_message(message, 36)
            time.sleep(5)
            display_message(time.strftime('%H:%M') + ' Uhr', 48)
            time.sleep(10)
            # display_message('AAAAAAA')
            # display_message('   AAAAA   ')


except IOError as e:
    logging.error(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    display_cleanup()
    logging.info("Display cleanup completed")
    logging.info("Program end")
    client.loop_stop()
    exit()
