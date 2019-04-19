import csv, time, requests, os, numpy.random, random
from datetime import datetime
import pathlib as pLib
import pandas as pd
import PIL
from PIL import Image, ImageDraw, ImageFont

#CONFIG
randomIntz = numpy.random.randint(4, size=10)

r = requests.get("https://finance.yahoo.com/quote/%5EDJI/components/")
stocks = pd.read_html("https://finance.yahoo.com/quote/%5EDJI/components/", header=0, parse_dates=["Symbol"])
tickerFile = 'ticker_' + str(randomIntz) + '.png'


def drawTicker():

    fnt = ImageFont.truetype("consola.ttf", 12)
    im = Image.new('RGBA', (800, 800), 'white')
    draw = ImageDraw.Draw(im)
    draw.text((25, 25), str(stocks), fill = 'black', font=fnt)
    im.save(tickerFile)

drawTicker()

def mainF():
    # Request sent for while loop

# While the website request is "OK"
    if (r.status_code == 200):
        # Grabs the table data from the website and parses
        df = pd.DataFrame(stocks)
        
        df.to_csv('stock.csv')
        print(stocks[0])

mainF()

#exit();