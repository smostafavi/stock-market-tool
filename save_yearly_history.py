import urllib
import urllib.request
from datetime import date
from datetime import datetime

def save_yearly_history(stock):
    year = str(date.today().year)
    lastyear = str(int(year) - 1)
    month = str(date.today().month)
    day = str(date.today().day)
    
    url = "http://real-chart.finance.yahoo.com/table.csv?s=" + stock + "&a=" + month +"&b=" + day + "&c=" + lastyear + "&d=" + month + "&e=" + day + "&f=" + year + "&g=d&ignore=.csv"

    htmlfile = ""
    htmlfile = urllib.request.urlopen(url, timeout=20)
    htmltext = str(htmlfile.read())

    htmltext = htmltext.replace("'", "")
    htmlrecords = htmltext.split("\\n")


    sfile = open("/home/vince/Documents/SWEN670/Database/stock_price_history/" + stock +".csv", "w")
    for x in htmlrecords:
        if (len(x) > 5):
            print(x, file=sfile)
    sfile.close()


