# This program will create a chart for bs with betas as columns and
#  percenage changes as column

from black_scholes import black_scholes

def create_black_scholes_chart():
    sp = 50.0
    print(",0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0")
    for p in list(-2.0, -1.0, 0.0, 1.0, 2.0):
        for b in list(0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0):
        

create_black_scholes_chart()
