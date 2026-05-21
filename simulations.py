#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:58:51 2026

@author: yuvianasachar

"""

import numpy as np

def monthly_portfolio(timeperiod, investment_per_month, rate):
    portfolio_history=[]
    portfolio_value=0
    monthly_rate=rate/12
   
    
    for month in range(timeperiod):
            portfolio_value+=investment_per_month
            portfolio_value*=(1+monthly_rate)
            portfolio_history.append(portfolio_value)
            
    portfolio_list=np.array(portfolio_history)
    portfolio_list=np.round(portfolio_list,2)
     
    return (portfolio_list) 

#----------------------------------#
 
def monthly_portfolio_step_up(timeperiod, investment_per_month, rate, s):
    
    portfolio_history_step = []

    portfolio_value = 0

    monthly_rate = rate / 12


    for month in range(1, timeperiod + 1):

        portfolio_value += investment_per_month

        portfolio_value *= (1 + monthly_rate)

        portfolio_history_step.append(portfolio_value)

        # Increase SIP every 12 months
        if month % 12 == 0 and month != timeperiod:

            investment_per_month *= (1 + s)


    portfolio_history_step = np.array(portfolio_history_step)

    portfolio_history_step = np.round(portfolio_history_step, 2)

    return portfolio_history_step

