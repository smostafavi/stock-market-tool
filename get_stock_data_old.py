import urllib
import urllib.request
import re

def get_stock_data(stock):
    url = "http://finance.yahoo.com/q?s=" + stock
    
    htmlfile = urllib.request.urlopen(url)
    htmltextr = htmlfile.read()
    htmltext = str(htmltextr)

    # get price
    regex = '<span id="yfs_l84_' + stock.lower() + '">(.+?)</span>'
    pattern = re.compile(regex)
    prices = re.findall(pattern, htmltext)
    print(prices)
    price = prices[0]

    # get price change
    regex = 'class="yfi-price-change-green">(.+?)</span>'
    pattern = re.compile(regex)
    pricechanges = re.findall(pattern, htmltext)
    print (regex)
    print(pricechanges)
    pricechange = pricechanges[0]

    # get beta
    regex = 'class="yfnc_tabledata1">(.+?)</td>'
    pattern = re.compile(regex)
    betas = re.findall(pattern, htmltext)
    print(betas)
    beta = betas[0]

    return (price, pricechange, beta)
    
