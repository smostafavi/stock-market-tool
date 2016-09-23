import os
path = "../../Database/stock_price_history/"
from datetime import date

from get_data_list import get_data_list
from vma_fma_buy_alert import vma_fma_buy_alert
from vma_sell_alert import vma_sell_alert
from trb_buy_alert import trb_buy_alert
from trb_sell_alert import trb_sell_alert


def calculate_total_return(stock, column, method, short_term, long_term, tolerance, hold_period=0, allow_multiple_buy=False):

    if not os.path.exists(os.path.join(os.getcwd(), "results")):
            os.makedirs(os.path.join(os.getcwd(), "results"))
    tot = 0

    try:
        ofile = os.path.join(os.getcwd(), "results", stock + "_" + column + "_"+ method + "_" + str(short_term) + "_" + str(long_term) + "_" + str(tolerance) + "_" + str(hold_period) + ".csv");
        tfile = open(ofile, "r")

        for x in tfile:
            fields = x.split(",")
            if len(fields) == 5:
                tot = tot + eval(fields[4])
    except:
        tot = 0

    return tot
            
