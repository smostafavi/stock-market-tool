import os.path
import sys
from get_options_data import get_options_data

def save_option_data(stock):
    try:
        if os.path.exists("/home/vince/Documents/SWEN670/Database/options/" + stock + ".csv"):
            ofile = open("/home/vince/Documents/SWEN670/Database/options/" + stock + ".csv", "a")
            newfile = "false"
        else:
            ofile = open("/home/vince/Documents/SWEN670/Database/options/" + stock + ".csv", "w")
            newfile = "true"

        options = get_options_data(stock)
        for x in options:
            if not((str(x[0][0]) == "d") and (newfile == "false")):
                if not((x[5] == "N/A") and (x[6] == "N/A")):
                    print(x[0] + "," + x[1] + "," + x[2] + "," + x[3]
                          + "," + x[4] +"," + x[5] + "," + x[6] + "," + x[7] + "," + x[8],
                          file = ofile)

    except:
        print("Unexpected error in save option data " + stock +": " + sys.exc_info()[0])

    ofile.close()
