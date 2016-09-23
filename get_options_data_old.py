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
    
    htmlfile = urllib.request.urlopen(url, timeout=10)
    htmltextr = htmlfile.read()
    htmltext = str(htmltextr)
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
    syear = str(year)
    month = date.today().month + 1
    smonth = str(month).zfill(2)

    return_results = list()
    return_results.append(["date/time", "stock", "symbol", "price", "strike", 
                           "bid", "ask", "black scholes call", "black shcoles put"])
    for strikeprice in strikeprices:
        row = list()
        row.append(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S"))
        row.append(stock)

        tempnum = round(eval(strikeprice) * 1000)
        sstrikeprice = str(tempnum).zfill(8)
        #symbol = stock + syear[2:3] + smonth + "15C" + "000" + str(strikeprice) + "00"
        symbol = stock + syear[2:4] + smonth + "15C" + sstrikeprice
        row.append(symbol)
        row.append(price[0])
        row.append(strikeprice)

        url = "http://finance.yahoo.com/q?s=" + symbol
        htmlfile = urllib.request.urlopen(url, timeout=10)
        htmltextr = htmlfile.read()
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

        return_results.append(row)
        
    return return_results
        

        

    
    
