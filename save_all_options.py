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
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " begin processing Save all options")

    hour = datetime.now().hour
    weekday = datetime.now().weekday()
    ifile = open("/home/pi/Desktop/LazarusPit/Database/stocks.txt", "r")

    for stock in ifile:
        stock = stock.replace("\n", "")            
        print(str(date.today().year) + "/" + str(date.today().month) +
               "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " begin processing " + stock)

        try:
            save_option_data(stock)
        except:
           print("Unexpected error in save all data " + stock +": " + sys.exc_info()[0]) 

        print(str(date.today().year) + "/" + str(date.today().month) +
               "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " end processing " + stock)
    
    ifile.close()
    print(str(date.today().year) + "/" + str(date.today().month) +
               "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " end processing  Save all options")

        
master()
    
