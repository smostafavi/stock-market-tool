import urllib
import urllib.request
import re
from find_between import find_between

def get_stock_data(stock):
    url = "http://fool.com/quote/" + stock
    
    htmlfile = urllib.request.urlopen(url)
    htmltextr = htmlfile.read()
    htmltext = str(htmltextr)
    htmltext = htmltext.replace("\\n", "")
    htmltext = htmltext.replace(" ", "")

    # get price
    price = eval(find_between('<h2class="current-price">$', '</h2>', htmltext))

    # get price change
    if (htmltext.find('<h2class="price-change-amountprice-pos">') != -1):       
        strpricechange = find_between('<h2class="price-change-amountprice-pos">', '</h2>', htmltext)
    else:
        strpricechange = find_between('<h2class="price-change-amountprice-neg">', '</h2>', htmltext)
    pricechange = eval(strpricechange.replace("$", ""))
    
    # open bid
    openprice = eval(find_between('<td>Open:</td><td>$', '</td>', htmltext))

    # volume
    volume = eval(find_between('<tdclass="table-label">Volume:</td><tdclass="update_volume">', '</td>', htmltext).replace(",", ""))

    # average volume
    avevolume = eval(find_between('<td>AvgVol</td><td>', '</td>', htmltext).replace(",", ""))

    # P/E ratio
    pe = eval(find_between('P/E<spanclass="small">(ttm)</span>:</td><td>', '</td>', htmltext))

    # dividend and yield
    dy =  find_between('<td>Div&amp;Yield:</td><td>$', '</td>', htmltext)
    div = eval(dy[:dy.index('(')])
    divyield = eval(find_between('(', '%)', dy)) / 100

    #eps
    eps = eval(find_between('EPS<spanclass="small">(ttm)</span>:</td><td>$', '</td>', htmltext))
    
    return (price, pricechange, openprice, volume, avevolume, pe, div, divyield, eps)
    
