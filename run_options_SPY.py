import os
import csv
from print_historical_analysis import print_historical_analysis
from get_data_list import get_data_from_dict_no_opts
from multiprocessing import Pool

def run_options_SPY():

    if not os.path.exists(os.path.join(os.getcwd(), "results")):
        os.makedirs(os.path.join(os.getcwd(), "results"))

    # read stock_price_history file into data dict and add index
    stock_data_dict = {}
    infile = csv.DictReader(open("../Database/stock_price_history/AXP.csv"))

    for idx,row in enumerate(infile):
        stock_data_dict[idx] = row
        
    datelist = get_data_from_dict_no_opts(stock_data_dict, "bDate")
    pricelist = get_data_from_dict_no_opts(stock_data_dict, "Close")
    
    pool = Pool()
    all_results = []
    
    print("Running, please wait...")
    
    for short in range(1, 201):
        all_results.append([pool.apply_async(print_historical_analysis, args=(stock_data_dict,datelist,pricelist,"VMA",short,short+long_delta,0.0,0,False)) for long_delta in range(1,200)])
    pool.close()
    pool.join()

    tfile = csv.writer(open(os.path.join(os.getcwd(), "results", "AXP_total_results" + ".csv"), "w"))
    for results in all_results:
        for result in results:
            r = result.get()
            tfile.writerow((r['short_term'],r['long_term'],r['total_return']))
    tfile.close()
    
    print("Finished writing results!")

run_options_SPY()
