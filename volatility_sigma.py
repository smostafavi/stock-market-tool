# Function name: volaitility sigma
# Description:  this function returns the standard deviation of
#    the daily returns. It uses adjusted close dates.

import statistics;

def volatility_sigma(stock):
    stock_file = open("/home/pi/Desktop/LazarusPit/Database/stock_price_history/" + stock + ".csv", "r")

    previous_return = 0
    returns = list()
    for stock_line in stock_file:
        
        values = stock_line.split(",")

        if (values[0] == "bDate" or values[0] == "Date" or stock_line == "\\n"):
            previous_return == 0
        elif previous_return == 0:
            previous_return = eval(values[6])
        else:
            returns.append((eval(values[6])- previous_return) / previous_return)
            previous_return = eval(values[6])

    return statistics.stdev(returns)
            
        
            
