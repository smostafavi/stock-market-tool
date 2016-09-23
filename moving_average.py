# Function name: moving average
# Description:  this function returns the moving average of a stock
#              You end the stock symbol and the number of days for the
#              average.  It uses the history prices for the last year.

import statistics;

def moving_average(stock, days):
    stock_file = open("/home/pi/Desktop/LazarusPit/Database/stock_price_history/" + stock + ".csv", "r")

    sum_prices = 0.0
    days_temp = days
    stock_file.readline()

    while days_temp > 0:
        stock_line = stock_file.readline();
        values = stock_line.split(",")        
        sum_prices = sum_prices + eval(values[6])
        days_temp = days_temp - 1

    return (sum_prices / days)
 
        
            
