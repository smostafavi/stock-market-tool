from get_data_list import get_data_list

def trb_sell_alert(stock, column, end_date, long_term):

    try:
        theList = get_data_list(stock, column, end_date, long_term+1)

        if theList[0] == min(theList):
            return True
    except:
        raise

    return False
