import os
import sys
#path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
path = "..//Database//stock_price_history//"

def get_data_list(stock, column, end_date, number_of_days, delay_days=0):

    #ifile = os.path.join(path, "data", stock + ".csv");
    ifile = os.path.join(path, stock + ".csv");

    try:
	    sfile = open(ifile, "r");
    except :
        raise

    columnIndex = -1
    records = 0
    skipped = 0
    foundDate = False
    theList = []

    for eachline in sfile:
        #print(eachline)
        splitline = eachline.rstrip().split(',')
        if not foundDate:
            if columnIndex == -1:
                for index in range(len(splitline)):
                    #print(" compare",splitline[index], column)
                    if splitline[index] == column:
                        columnIndex = index
            else:
                if splitline[0] == end_date or number_of_days == -1:
                    foundDate = True
        if foundDate:
            if skipped < delay_days:
                skipped = skipped + 1
            elif records < number_of_days or number_of_days == -1:
                if column != "bDate":
                    theList.append(float(splitline[columnIndex]))
                else:
                    theList.append(splitline[columnIndex])
                records = records + 1

    sfile.close()

    if columnIndex == -1:
        print("ERROR: Column '" + column + "' not found in " + stock + ".csv", end='\n')
        return []
    elif records == 0:
        print("ERROR: End date '" + end_date + "' not found in " + stock + ".csv", end='\n')
        return []
    elif records < number_of_days and number_of_days != -1:
        print("ERROR: Insufficient data for " + str(number_of_days) + " records in " + stock + ".csv - found " + str(records), end='\n')
        return []
    else:
        return theList
