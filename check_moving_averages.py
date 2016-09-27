from datetime import date
from datetime import datetime
import time

def check_moving_averages(stock):
    print(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " begin check moving averages")

    ifile = open("/home/vince/Documents/SWEN670/Database/moving_averages/" + stock + ".csv", "r")

    lastdate = ""
    last10chg = ""
    last20chg = ""
    currentdate = ""
    current10chg = ""
    current20chg = ""
    for x in ifile:
        x = x.replace("\n", "")
        fields = x.split(",")
        print(fields)
        if not(currentdate == fields[0]):
            lastdate = currentdate
            last10chg = current10chg
            last20chg = current20chg

            currentdate = fields[0]
            current10chg = fields[4]
            current20chg = fields[5]

    print(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + "  comparing " +
                   lastdate + " (" + last10chg + " " + last20chg +")  to " + currentdate + " (" +
                   current10chg + " " + current20chg + ")")
    # check if passed moving averages
    if ((last10chg == 'lower' or last20chg == 'lower') and
        ((current10chg == 'higher') or (current20chg == 'higer'))):
        ofile = open("/home/vince/Documents/SWEN670/Database/buys/moving_averages.csv", "a")
        print(currentdate + "," + stock +"," + current10chg +
              "," + current20chg + "," + last10chg + "," + last20chg, file=ofile )
        ofile.close()

    ifile.close()
    print(str(date.today().year) + "/" + str(date.today().month) +
                   "/" + str(date.today().day) + " " + time.strftime("%H:%M:%S") + " end check moving averages")
