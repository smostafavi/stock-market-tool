from save_option_data import save_option_data
from datetime import date
from datetime import datetime
from moving_average import moving_average
from save_moving_averages import save_moving_averages
import time
import sys
from check_moving_averages import check_moving_averages
from save_yearly_history import save_yearly_history

def master():

    print(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " begin processing")

    hour = datetime.now().hour
    weekday = datetime.now().weekday()
    ifile = open("/home/pi/Desktop/LazarusPit/Database/stocks.txt", "r")

    for stock in ifile:
        stock = stock.replace("\n", "")            
        print(str(date.today().year) + "/" + str(date.today().month) +
               "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " begin processing " + stock)

        # only get option data during market hours
        if ((hour >= 9) & (hour <= 16) & (weekday in [0, 1, 2, 3, 4])):
            try:
                save_option_data(stock)
            except Exception as e:
                print("Error " + stock + " save option data " + e)

        # run moving averages after market closes
        if ((hour == 17) & (weekday in [0, 1, 2, 3, 4])):
            try:
                save_moving_averages(stock)
            except Exception as e:
                print("Error " + stock + " save moving averages " + e)

            try:
                save_yearly_history(stock)
            except Exception as e:
                print("Error " + stock + " save yearly history " + e)
                    

        # check moving averages after market closes
        if ((hour == 18) & (weekday in [0, 1, 2, 3, 4])):
            try:
                check_moving_averages(stock)
            except Exception as e:
                print("Error " + stock + " check moving averages " + e)
                    

        print(str(date.today().year) + "/" + str(date.today().month) +
               "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " end processing " + stock)
    
    ifile.close()
    print(str(date.today().year) + "/" + str(date.today().month) +
               "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " end processing")

        
master()
    
