# !/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from display import display_init, display_message, display_cleanup, display_sleep
import paho.mqtt.client as mqtt
from queue import Queue

# MessageQueue anlegen
mq = Queue()

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

# Create MQTT-Client
mqtt_client = mqtt.Client("StatusPI")


def on_message(client, userdata, raw_msg):
    payload = str(raw_msg.payload.decode("utf-8"))
    mq.put(payload)
    logging.debug("Message: " + payload)


def on_log(client, userdata, level, buf):
    logging.debug("Log: " + buf)


try:
    do_update = False
    run_cnt = 0
    refresh_every = 3

    display_init()
    logging.debug("Display init completed")

    mqtt_client.on_message = on_message
    mqtt_client.on_log = on_log
    logging.info("MQTT Client started")

    mqtt_client.connect(host="raspi4", port=1883, keepalive=60)
    logging.info("Client connected")

    mqtt_client.subscribe("iob/0_userdata/0/mqtt_messages/info")
    logging.debug("Client subscribed")

    mqtt_client.loop_start()
    logging.debug("Client loop startes")

    while True:

        while not mq.empty():
            message = mq.get()
            if message is None:
                continue
            run_cnt += 1
            logging.info("Run: " + str(run_cnt))

            logging.info("Output: " + message)
            display_message(message, 36)
            time.sleep(10)

            display_message(time.strftime('%H:%M') + ' Uhr', 48)
            time.sleep(15)

            # if run_cnt % refresh_every == 0:
            #     logging.info("Display-Refresh")
            #     display_init()


except IOError as e:
    logging.error(e)

except KeyboardInterrupt:
    logging.debug("ctrl + c:")
    display_cleanup()
    logging.debug("Display cleanup completed")
    logging.debug("Program end")
    mqtt_client.loop_stop()
    exit()
