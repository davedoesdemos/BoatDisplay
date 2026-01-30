#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
libdir = "/home/lustyd/epaper/e-Paper/RaspberryPi_JetsonNano/python/lib/"
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3e
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in3e Demo")

    epd = epd7in3e.EPD()   
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    
    # read bmp file 
    logging.info("2.read bmp file")
    Himage = Image.open('./youtube.png')
    epd.display(epd.getbuffer(Himage))
    time.sleep(30)
    
    logging.info("Clear...")
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3e.epdconfig.module_exit(cleanup=True)
    exit()
