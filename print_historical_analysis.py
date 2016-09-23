import os
#path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
path = "../../Database/stock_price_history/"
from datetime import date

from get_data_list import get_data_list
from vma_fma_buy_alert import vma_fma_buy_alert
from vma_sell_alert import vma_sell_alert
from trb_buy_alert import trb_buy_alert
from trb_sell_alert import trb_sell_alert


def print_historical_analysis(stock, column, method, short_term, long_term, tolerance, hold_period=0, allow_multiple_buy=False):

    if not os.path.exists(os.path.join(os.getcwd(), "results")):
            os.makedirs(os.path.join(os.getcwd(), "results"))

    ofile = os.path.join(os.getcwd(), "results", stock + "_" + column + "_"+ method + "_" + str(short_term) + "_" + str(long_term) + "_" + str(tolerance) + "_" + str(hold_period) + ".csv");
    tfile = open(ofile, "w")

    datelist = get_data_list(stock, "bDate", "", -1)
    pricelist = get_data_list(stock, column, "", -1)
    buyDates = []
    buyPrices = []
    lastActionSell = True
    daysSinceBuy = len(datelist)
    trbDaysSinceBuy = []

    for x in range(len(datelist)-long_term-1,-1,-1): #going forwards in time, starting with the latest date that will have data.
        if method == "VMA":
            if vma_fma_buy_alert(stock, column, datelist[x], short_term, long_term, tolerance):
                buyDates.append(datelist[x])
                buyPrices.append(pricelist[x])
                lastActionSell = False
            elif vma_sell_alert(stock, column, datelist[x], short_term, long_term, tolerance) and not lastActionSell:
                if allow_multiple_buy: # Print all buys
                    for y in range(0,len(buyDates)):
                        tfile.write(buyDates[y] + "," + str(buyPrices[y]) + "," + datelist[x] + "," + str(pricelist[x]) + "," + str((pricelist[x]-buyPrices[y])/buyPrices[y]) + "\n")
                else: # Print only the first buy.
                    tfile.write(buyDates[0] + "," + str(buyPrices[0]) + "," + datelist[x] + "," + str(pricelist[x]) + "," + str((pricelist[x]-buyPrices[0])/buyPrices[0]) + "\n")
                buyDates = []
                buyPrices = []
                lastActionSell = True
        elif method == "FMA":
            if vma_fma_buy_alert(stock, column, datelist[x], short_term, long_term, tolerance):
                if allow_multiple_buy or daysSinceBuy >= hold_period:
                    if x < hold_period:
                        tfile.write(datelist[x] + "," + str(pricelist[x]) + ",holding\n")
                    else:
                        tfile.write(datelist[x] + "," + str(pricelist[x]) + "," + datelist[x-hold_period] + "," + str(pricelist[x-hold_period]) + "," + str((pricelist[x-1-hold_period]-pricelist[x-1])/pricelist[x-1]) + "\n")
                    daysSinceBuy = 0
            daysSinceBuy = daysSinceBuy + 1
        elif method == "TRB":
            if trb_buy_alert(stock, column, datelist[x], long_term):
                buyDates.append(datelist[x])
                buyPrices.append(pricelist[x])
                lastActionSell = False
                trbDaysSinceBuy.append(0)
            elif trb_sell_alert(stock, column, datelist[x], long_term) and not lastActionSell and trbDaysSinceBuy[0] >= hold_period:
                if allow_multiple_buy: # Print all buys held at least hold_period
                    keep_looping = True
                    while keep_looping:
                        print(trbDaysSinceBuy)
                        if trbDaysSinceBuy[0] >= hold_period:
                            tfile.write(buyDates[0] + "," + str(buyPrices[0]) + "," + datelist[x] + "," + str(pricelist[x]) + "," + str((pricelist[x]-buyPrices[0])/buyPrices[0]) + "\n")
                            del buyDates[0]
                            del buyPrices[0]
                            del trbDaysSinceBuy[0]
                            keep_looping = len(trbDaysSinceBuy) > 0
                        else:
                            keep_looping = False
                else: # Print only the first buy, clear the tables.
                    tfile.write(buyDates[0] + "," + str(buyPrices[0]) + "," + datelist[x] + "," + str(pricelist[x]) + "," + str((pricelist[x]-buyPrices[0])/buyPrices[0]) + "\n")
                    buyDates = []
                    buyPrices = []
                    trbDaysSinceBuy = []
                lastActionSell = True
            trbDaysSinceBuy[:] = [ele +1 for ele in trbDaysSinceBuy]

    if not len(buyDates) == 0:   #Bought something and didn't sell it yet.  Print holding.
        if allow_multiple_buy: # Print all buys
            for y in range(0,len(buyDates)):
                tfile.write(buyDates[y] + "," + str(buyPrices[y]) + ",holding\n")
        else: # Print only the first buy.
            tfile.write(buyDates[0] + "," + str(buyPrices[0]) + ",holding\n")

    tfile.close()
