import os
from calculate_total_return import calculate_total_return
from print_historical_analysis import print_historical_analysis
import datetime

def run_options_SPY():

    if not os.path.exists(os.path.join(os.getcwd(), "results")):
        os.makedirs(os.path.join(os.getcwd(), "results"))

    ofile = os.path.join(os.getcwd(), "results", "SP500_total_results" + ".csv");
    

    print("Beginning", str(datetime.datetime.now()))
    for short in range(1, 201):
        for long_delta in range(1, 200):
            tfile = open(ofile, "a")
            print_historical_analysis("SP500", "Close", "VMA", short, (short + long_delta), 0.0, 0, False)
            total_return = calculate_total_return("SP500", "Close", "VMA", short, (short + long_delta),0.0, 0, False)

            print(str(short) + "," + str(short + long_delta) + "," + str(total_return) + "," + str(datetime.datetime.now()))
            print(str(short) + "," + str(short + long_delta) + "," + str(total_return), file=tfile)             
            tfile.close()

run_options_SPY()
