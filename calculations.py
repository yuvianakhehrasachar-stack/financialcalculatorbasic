#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:52:57 2026

@author: yuvianasachar

"""



def initial_investment(investment_per_month,timeperiod):
    total_investment=investment_per_month*timeperiod
    return total_investment

#----------------------------------#

def sip_calculator_at_the_end(investment_per_month,goal,timeperiod,rate):
    """ Using these values, we cab calculate the basic SIP amount
    For the lowest possible rate from portfolio allocation"""
    monthly_rate=rate/12
    maturity_value=float(investment_per_month*(((1+monthly_rate)**timeperiod-1)/monthly_rate)*(1+monthly_rate))
    return round(maturity_value,2)
    return maturity_value

#----------------------------------#

# print("For a total investment of",'₹',initial_investment(investment_per_month, timeperiod),)
# print("If you recieve the lowest possible rate your maturity value at the end of the investing term could be: ₹", sip_calculator_at_the_end(investment_per_month, goal, timeperiod, lowest_possible_rate))
# print("If you recieve the highest possible rate your maturity value at the end of the investing term could be: ₹",sip_calculator_at_the_end(investment_per_month, goal, timeperiod, highest_possible_rate))
# biggest_maturity=sip_calculator_at_the_end(investment_per_month, goal, timeperiod, highest_possible_rate)
# total_invested=initial_investment(investment_per_month, timeperiod)

# print("You could earn in interest:",'₹',round(biggest_maturity-total_invested,2))
# print("")
# print('-------------------------')
 
