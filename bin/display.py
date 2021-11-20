#!/usr/bin/env python3

import time
from PIL import Image, ImageDraw, ImageFont
import lib.oled.SSD1331 as SSD1331

class Display:
    disp = SSD1331.SSD1331()
    nextFrame = Image.new("RGB", (disp.width, disp.height), "BLACK")
    
    def __init__(self):
        # Initialize library.
        self.disp.Init()
        # Clear display.
        self.disp.clear()
        
    def __del__(self):
        self.disp.clear()
        self.disp.reset()
        
    def ShowImage(self, filePath):
        image = Image.open(filePath)
        self.disp.ShowImage(image, 0, 0)
        
    def NewFrame(self, bgColor):
        self.nextFrame = Image.new("RGB", (self.disp.width, self.disp.height), bgColor)
        draw = ImageDraw.Draw(self.nextFrame)
        return draw
        
    def ShowFrame(self):
        self.disp.ShowImage(self.nextFrame, 0, 0)
        

def oledtest():
    disp = SSD1331.SSD1331()

    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    
    disp.drawLine(1,1,40,40)
    time.sleep(1)

    # Create blank image for drawing.
    image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    fontLarge = ImageFont.truetype('./lib/oled/Font.ttf', 20)
    fontSmall = ImageFont.truetype('./lib/oled/Font.ttf', 13)

    print("- draw line")
    draw.line([(0, 0), (0, 63)], fill="BLUE", width=5)
    draw.line([(0, 0), (95, 0)], fill="BLUE", width=5)
    draw.line([(0, 63), (95, 63)], fill="BLUE", width=5)
    draw.line([(95, 0), (95, 63)], fill="BLUE", width=5)

    print("- draw rectangle")
    draw.rectangle([(5, 5), (90, 30)], fill="BLUE")

    print("- draw text")
    draw.text((8, 0), u'Hello', font=fontLarge, fill="WHITE")
    draw.text((12, 40), 'World !!!', font=fontSmall, fill="BLUE")

    # image1 = image1.rotate(45)
    disp.ShowImage(image1, 0, 0)
    time.sleep(2)

    disp.clear()
    disp.reset()

def test():
    print('\nThe OLED screen test.')
    oledtest()


if __name__ == "__main__":
    test()

