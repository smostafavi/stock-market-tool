from moving_average import moving_average
import urllib
import urllib.request
import re
from datetime import date
import time
from remove_duplicate_values import remove_duplicate_values
import os.path
import sys

def save_moving_averages(stock):
    url = "http://finance.yahoo.com/q/op?s=" + stock + "+Options"

    print(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " url " + url) 

    htmltext = ""
    try:
        htmlfile = urllib.request.urlopen(url, timeout=15)
        htmltextr = htmlfile.read()
        htmltext = str(htmltextr)
    except Exception as e:
        print("Error in get_options_data")
        print("error geting options page" + stock)
        print(e)
        
    regex = '<span id="yfs_l84_' + stock + '" data-sq="' + stock + ':value">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)

    try:
        if os.path.exists("/home/pi/Desktop/LazarusPit/Database/moving_averages/" + stock + ".csv"):
            ofile = open("/home/pi/Desktop/LazarusPit/Database/moving_averages/" + stock + ".csv", "a")
            newfile = "false"
        else:
            ofile = open("/home/pi/Desktop/LazarusPit/Database/moving_averages/" + stock + ".csv", "w")
            print("date,price,10 day, 20 day, 10 day compare, 20 day compare", file = ofile)
            newfile = "true"

        ten_day = moving_average(stock, 10)
        twenty_day = moving_average(stock, 20)
        if (float(price[0]) > ten_day):
            ten_day_str = "higher"
        else:
            ten_day_str = "lower"

        if (float(price[0]) > twenty_day):
            twenty_day_str = "higher"
        else:
            twenty_day_str = "lower"
        
        print(str(date.today().year) + "/" + str(date.today().month) +
              "/" + str(date.today().day) + "," +
              str(price[0]) + "," + str(ten_day) + "," +
              str(twenty_day) + "," + ten_day_str + "," + twenty_day_str, file = ofile)
    except:
        print("Unexpected error in save moving averages " + stock +": " + sys.exc_info()[0])

    ofile.close()
