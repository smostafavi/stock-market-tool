import os
import csv
from calculate_total_return import calculate_total_return
from print_historical_analysis import print_historical_analysis
import datetime

def run_options_SPY():

    if not os.path.exists(os.path.join(os.getcwd(), "results")):
        os.makedirs(os.path.join(os.getcwd(), "results"))

    # only need to open this file once for appending and close at finish    
    ofile = os.path.join(os.getcwd(), "results", "AXP_total_results" + ".csv");
    tfile = open(ofile, "w")

    # read stock_price_history file into data dict and add index
    stock_data_dict = {}
    infile = csv.DictReader(open("../Database/stock_price_history/AXP.csv"))

    for idx,row in enumerate(infile):
      stock_data_dict[idx] = row
    
    print("Beginning", str(datetime.datetime.now()))
    for short in range(1, 201):
        for long_delta in range(1, 201):
            total_return = print_historical_analysis(stock_data_dict, "AXP", "Close", "VMA", short, (short + long_delta), 0.0, 0, False)
            #total_return = calculate_total_return("AXP", "Close", "VMA", short, (short + long_delta),0.0, 0, False)

            #print(str(short) + "," + str(short + long_delta) + "," + str(total_return) + "," + str(datetime.datetime.now()))
            print(str(short) + "," + str(short + long_delta) + "," + str(total_return), file=tfile)             
    tfile.close()

run_options_SPY()
