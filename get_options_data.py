import urllib
import urllib.request
import re
from datetime import date
import time
from remove_duplicate_values import remove_duplicate_values
from black_scholes import black_scholes
from volatility_sigma import volatility_sigma

def get_options_data(stock):
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
    
    htmltext = htmltext[htmltext.find(stock + '&strike='):]
    regex = stock + '&strike=(.+?)">'
    pattern = re.compile(regex)
    strikeprices = re.findall(pattern, htmltext)
    strikeprices = remove_duplicate_values(strikeprices)
    sigma = volatility_sigma(stock)

    year = date.today().year
    
    month = date.today().month  
    if month == 12:
        month = 1
        year = year + 1
    else:
        month = month + 1
    syear = str(year)
    smonth = str(month).zfill(2)


    # find 3rd Friday
    fridayCount = 0
    dayCount = 0
    while fridayCount < 3:
        dayCount = dayCount + 1
        testDate = date(year, month, dayCount)
        if testDate.weekday() == 4:
            fridayCount = fridayCount + 1
    
    return_results = list()
    return_results.append(["date/time", "stock", "symbol", "price", "strike", 
                           "bid", "ask", "black scholes call", "black shcoles put"])
    for strikeprice in strikeprices:
        print("strikeprice ", strikeprice)
        row = list()
        row.append(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S"))
        row.append(stock)

        tempnum = round(eval(strikeprice) * 1000)
        sstrikeprice = str(tempnum).zfill(8)
        #symbol = stock + syear[2:3] + smonth + "15C" + "000" + str(strikeprice) + "00"
        symbol = stock + syear[2:4] + smonth + str(dayCount) + "C" + sstrikeprice
        row.append(symbol)
        row.append(price[0])
        row.append(strikeprice)

        url = "http://finance.yahoo.com/q?s=" + symbol
        print(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " url " + url)

        foundSite = True
        try:
            htmlfile = urllib.request.urlopen(url, timeout=15)
            htmltextr = htmlfile.read()
        except Exception as e:
            print("Error in get_options_data")
            print("cannot find " + url + " ")
            print(e)
            foundSite = False
            
        print(str(date.today().year) + "/" + str(date.today().month) +
                "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " found url " + url)
        if (foundSite == True):
            
            htmltext = str(htmltextr)
            # get bid price
            regex = '<span id="yfs_b00_' + symbol.lower() + '">(.+?)</span>'

            pattern = re.compile(regex)
            bid = re.findall(pattern, htmltext)
            if len(bid) > 0:
                row.append(bid[0])
            else:
                row.append("N/A")

            # get ask price
            regex = '<span id="yfs_a00_' + symbol.lower() + '">(.+?)</span>'
            pattern = re.compile(regex)
            ask = re.findall(pattern, htmltext)
            if len(ask) > 0:
                row.append(ask[0])
            else:
                row.append("N/A")
            callPrice, putPrice = black_scholes(float(price[0]), float(strikeprice),
                                        25.0, 0.0, sigma, 0.01)
            row.append(callPrice)
            row.append(putPrice)

            print(str(date.today().year) + "/" + str(date.today().month) +
                    "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " exit get options " + stock)

            return_results.append(row)
        
    return return_results
        

        

    
    
