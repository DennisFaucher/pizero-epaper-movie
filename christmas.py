#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
#DMF next line
import glob
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V2 Demo")
    
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
# Christmas Images for Loop
    for filepath in sorted(glob.iglob('/home/pi/Pictures/Frosty/*.bmp')):
        # read image, sleep 2 seconds
        logging.info("2.read bmp file...")
        image = Image.open(filepath)
        epd.display(epd.getbuffer(image))
        time.sleep(60)
    for filepath in sorted(glob.iglob('/home/pi/Pictures/Miser/*.bmp')):
        # read image, sleep 2 seconds
        logging.info("2.read bmp file...")
        image = Image.open(filepath)
        epd.display(epd.getbuffer(image))
        time.sleep(60)
    for filepath in sorted(glob.iglob('/home/pi/Pictures/Nightmare/*.bmp')):
        # read image, sleep 2 seconds
        logging.info("2.read bmp file...")
        image = Image.open(filepath)
        epd.display(epd.getbuffer(image))
        time.sleep(60)
    for filepath in sorted(glob.iglob('/home/pi/Pictures/Charlie/*.bmp')):
        # read image, sleep 2 seconds
        logging.info("2.read bmp file...")
        image = Image.open(filepath)
        epd.display(epd.getbuffer(image))
        time.sleep(60)

# Happy Holidays
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0,0),(249,120)],outline = 0)
    draw.rectangle([(1,1),(248,119)],outline = 0)
    draw.rectangle([(2,2),(247,118)],outline = 0)
    draw.rectangle([(3,3),(246,117)],outline = 0)
    draw.rectangle([(4,4),(245,116)],outline = 0)
    draw.text((40, 50), 'Happy Holidays!', font = font24, fill = 0)
    epd.display(epd.getbuffer(image))
    time.sleep(2)

    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
