
from math import sqrt, exp, log, erf

from decimal import *

def black_scholes(undprice, strike, time, rate, sigma, divrate):
    getcontext().prec = 5

    #inputs
    #undprice = float(84.88)  # S
    #strike = float(60.00)      # K
    #time = float(25)         # time until expr in days
    #rate = float(.0025)          # risk free rate
    #sigma = float(.01)        # stand deviation of stock's return
    #divrate = float(0.017)      # dividend yield

    #statistics
    sigTsquared = sqrt(Decimal(time)/356) * sigma
    edivT = exp((-divrate * time) /356)
    ert = exp((-rate * time) / 356)
    d1 = (log(undprice * edivT / strike) + (rate + 0.5 * (sigma ** 2)) * time/356)/sigTsquared
    d2 = d1 - sigTsquared
    Nd1 = (1 + erf (d1/sqrt(2)))/2
    Nd2 = (1 + erf (d2/sqrt(2)))/2
    iNd1 = (1 + erf (-d1/sqrt(2)))/2
    iNd2 = (1 + erf (-d2/sqrt(2)))/2

    #Output
    callPrice = round(undprice * edivT * Nd1 - strike * ert * Nd2, 2)
    putPrice = round(strike * ert * iNd2 - undprice * edivT * iNd1, 2)

    return (str(callPrice), str(putPrice))

