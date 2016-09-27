from get_data_list import get_data_list, get_data_from_dict

def new_vma_fma_buy_alert(stock_data_dict, column, end_date, short_term, long_term, tolerance):

    shortList = get_data_from_dict(stock_data_dict, column, end_date, short_term+1)
    shortSum = sum(shortList)
    longList = get_data_from_dict(stock_data_dict, column, end_date, long_term+1)
    longSum = sum(longList)

    yesterdayShort = (shortSum - shortList[0]) / short_term
    yesterdayLong = (longSum - longList[0]) / long_term
    todayShort = (shortSum - shortList[len(shortList)-1]) / short_term
    todayLong = (longSum - longList[len(longList)-1]) / long_term

    if todayShort >= (todayLong * (1+tolerance)):
      if yesterdayShort < (yesterdayLong * (1+tolerance)):
        return True

    return False


def vma_fma_buy_alert(stock, column, end_date, short_term, long_term, tolerance):

    try:
        # For performance, gather list for both today and yesterday in one
        # call, rather than gathering two separate lists.  We'll subtract the
        # first or last item in the list to get the appropriate data set later.
        shortList = get_data_list(stock, column, end_date, short_term+1)
        shortSum = sum(shortList)
        longList = get_data_list(stock, column, end_date, long_term+1)
        longSum = sum(longList)

        # Yesterday's data = the list - the first item in the list.
        yesterdayShort = (shortSum - shortList[0])/short_term
        yesterdayLong = (longSum - longList[0])/long_term
        # Today's data = the list - the last item in the list.
        todayShort = (shortSum - shortList[len(shortList)-1])/short_term
        todayLong = (longSum - longList[len(longList)-1])/long_term

        if todayShort >= (todayLong * (1+tolerance)):
            if yesterdayShort < (yesterdayLong * (1+tolerance)):
                return True
    except:
        raise

    return False
