# !/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from display import display_init, display_message, display_cleanup

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("MQTT Client start")

    display_init()

    while True:
        display_message(time.strftime('%H:%M:%S'))
        time.sleep(1)


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    logging.info("MQTT Client end")
    display_cleanup()
    exit()
