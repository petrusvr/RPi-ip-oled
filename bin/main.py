#!/usr/bin/env python3

import time
from PIL import ImageDraw, ImageFont
from datetime import datetime
import display as OLED
import ip as Net
import RPi.GPIO as GPIO

doRun = True

def buttonPressed(channel):
    global doRun
    print("Button pressed on GPIO="+str(channel),"Stopping programm!")
    doRun = False;
    
def main():
    global doRun
    GPIO.setmode(GPIO.BCM)                             
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(5, GPIO.RISING, callback=buttonPressed)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(6, GPIO.RISING, callback=buttonPressed)

    fontxSmall = ImageFont.truetype('./lib/oled/Font.ttf', 12)
    fontxxSmall = ImageFont.truetype('./lib/oled/Font.ttf', 10)
    
    oled = OLED.Display()
    
    oled.ShowImage('./resources/pwr.bmp')
    time.sleep(5)
    
    oled.ShowImage('./resources/lab.bmp')
    time.sleep(5)
    
    # counter
    ips = Net.IpReader.getIps()
    while doRun:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        if now.second % 5 == 0:
            ips = Net.IpReader.getIps()
            print("Reading ips", ips)
        
        ints = list(ips.keys())
        
        draw = oled.NewFrame("BLACK")
        draw.text((0, 0), ints[0], font=fontxSmall, fill="YELLOW")
        draw.text((0, 13), ips[ints[0]], font=fontxSmall, fill="YELLOW")   
        draw.text((0, 27), ints[1], font=fontxSmall, fill="GREEN")
        draw.text((0, 41), ips[ints[1]], font=fontxSmall, fill="GREEN")
        
        draw.text((50, 64-11), current_time, font=fontxxSmall, fill="GRAY")
        
        oled.ShowFrame()
        time.sleep(0.5)
    
    del oled    
    GPIO.cleanup()


if __name__ == "__main__":
    main()


