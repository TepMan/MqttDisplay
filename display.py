import os
import sys

from lib.waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13_V2.EPD()
resourceDir = 'pic'
libDir = 'lib'

if os.path.exists(libDir):
    sys.path.append(libDir)


def display_message(message, fontsize):
    font = ImageFont.truetype(os.path.join(resourceDir, 'Font.ttc'), fontsize)
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(image))
    epd.init(epd.PART_UPDATE)

    # epd.with ist die Höhe, epd.height ist die Breite!!!
    middle_width = epd.width / 2
    middle_height = epd.height / 2

    # draw.rectangle([(0, 0), (248, 120)], outline=0)

    # draw.line([(0, middle_width), (epd.height, middle_width)])
    # draw.line([(middle_height, 0), (middle_height, epd.height)])

    draw.text((epd.width, middle_width), message, font=font, fill=0, anchor="mm")

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
    # epd2in13_V2.epdconfig.module_exit()

