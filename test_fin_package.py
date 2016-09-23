p = ".\\yahoo_finance-1.1.4\\yahoo_finance"
from p import Share

def test_fin_package():
    yahoo = Share('YHOO')
    print yahoo.get_open()
    
    print yahoo.get_price()
    
    print yahoo.get_trade_datetime()

test_fin_package()
