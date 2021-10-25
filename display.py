import os
import sys

from lib.waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13_V2.EPD()
resourceDir = 'pic'
libDir = 'lib'

if os.path.exists(libDir):
    sys.path.append(libDir)


def display_message(message):
    # Drawing on the image
    font24 = ImageFont.truetype(os.path.join(resourceDir, 'Font.ttc'), 24)
    font36 = ImageFont.truetype(os.path.join(resourceDir, 'Font.ttc'), 36)

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(image))
    epd.init(epd.PART_UPDATE)

    draw.rectangle([(0, 0), (248, 120)], outline=0)
    draw.text((50, 45), message, font=font36, fill=0)

    image = image.transpose(Image.ROTATE_180)
    epd.displayPartial(epd.getbuffer(image))


def display_sleep():
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    epd.sleep()


def display_init():
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)


def display_cleanup():
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    display_sleep()
    epd2in13_V2.epdconfig.module_exit()

