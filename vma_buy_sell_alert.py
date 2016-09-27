from get_data_list import get_data_from_dict

def vma_buy_sell_alert(stock_data_dict, column, end_date, short_term, long_term, tolerance):
    
    shortList = get_data_from_dict(stock_data_dict, column, end_date, short_term+1)
    shortSum = sum(shortList)
    longList = get_data_from_dict(stock_data_dict, column, end_date, long_term+1)
    longSum = sum(longList)

    yesterdayShort = (shortSum - shortList[0]) / short_term
    yesterdayLong = (longSum - longList[0]) / long_term
    todayShort = (shortSum - shortList[len(shortList)-1]) / short_term
    todayLong = (longSum - longList[len(longList)-1]) / long_term

    if ((todayShort >= (todayLong * (1+tolerance))) and (yesterdayShort < (yesterdayLong * (1+tolerance)))):
      return "buy"
    elif ((todayShort < (todayLong * (1-tolerance))) and (yesterdayShort >= (yesterdayLong * (1-tolerance)))):
      return "sell"

    return ""
