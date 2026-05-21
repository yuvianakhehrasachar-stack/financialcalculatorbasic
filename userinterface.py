#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:13:36 2026

@author: yuvianasachar
"""

from calculations import sip_calculator_at_the_end
from allocations import allocationz
from allocations import allocations



 
    
def user_input():
    
    investment_per_month=float(input("How much would you like to invest monthly (in rupees)?: "))
    # goal=float(input("Great! What is your financial goal? Enter the amount of money you would like to recieve at the end of the investing term: "))
    timeperiod=int(input("Cool! Enter the time period you have for this investment in MONTHS: "))
    risk=int(input("Lovely! And from a scale of 1-10, how much risk are you willing to take with 1 being no risk at all and 10 being as risky as it gets?: "))
    return investment_per_month,timeperiod,risk
       

 


   
    
    