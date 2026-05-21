#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:19:29 2026

@author: yuvianasachar
"""

from userinterface import user_input
from allocations import allocations, allocationz
from calculations import initial_investment
from calculations import sip_calculator_at_the_end
from simulations import monthly_portfolio
from simulations import monthly_portfolio_step_up
import matplotlib.pyplot as plt
import numpy as np


goal=0
print("Welcome to the very basic SIP Calculator for Indian Markets/Mutual Funds")
print('')
print("It just calculates how much money you could make off of your investments based on the amount of risk you're willing to take")
print("")
print("The rates and allocation amounts are based on averages. The calculator doesn't give any real financial advice (yet) ")
print("")
print("Let's get started!")
print('-----------------------') 

while True:
   
    print("Enter | 1. Basic SIP Calculator and Risk Allocation | 2. Step Up SIP Calculator | 3. Graph Portfolio | 4. Exit")
    choice1=int(input(" "))
    
    
    if choice1==1:
       investment_per_month, timeperiod, risk = user_input()

       risk_profile, highest_possible_rate, lowest_possible_rate, risk = allocationz(risk)

       portfolio = allocations[risk_profile]
        
       print("Based on your risk appetite you have been alloted this portfolio")
       print("-------------------------")
       for fund_type, percentage in portfolio.items():
               amount=investment_per_month*percentage
               
               print(fund_type,":","₹",amount)
       print('If you got the highest possible rate your matrurity value could be:',sip_calculator_at_the_end(investment_per_month, goal, timeperiod, highest_possible_rate))
       print('If you got the lowest possible rate your maturity value could be:',sip_calculator_at_the_end(investment_per_month, goal, timeperiod, lowest_possible_rate))
       print("This is based on an initial investment of: ", initial_investment(investment_per_month, timeperiod))
       
       
    elif choice1==2:
        s=int(input("By how much would you like to increase your SIP every year? Enter in decimal eg 5% is 0.05: "))
        print("If you got the highest possible rate, your new portfolio value would be:",monthly_portfolio_step_up(timeperiod, investment_per_month, highest_possible_rate, s))
        print("If you got the lowest possible rate, your new portfolio value would be:",monthly_portfolio_step_up(timeperiod, investment_per_month, lowest_possible_rate, s))


    elif choice1==3:
        investment_per_month, timeperiod, risk = user_input()

        risk_profile, highest_possible_rate, lowest_possible_rate, risk = allocationz(risk)

        portfolio = allocations[risk_profile]
        
        s=int(input("By how much would you like to increase your SIP every year? Enter in percent eg: 5% = 5 "))
        s=s/100
        
        portfolio_list=monthly_portfolio(timeperiod, investment_per_month, (highest_possible_rate+lowest_possible_rate)/2)
        portfolio_history_step=monthly_portfolio_step_up(timeperiod, investment_per_month, (highest_possible_rate+lowest_possible_rate)/2, s)
        
        plt.plot(portfolio_history_step, label='With step up')
        plt.plot(portfolio_list, label='Without step up')
        
        plt.xlabel("Months")
        plt.ylabel("Growth")
        plt.title("Portfolio Growth Over Time")
        plt.legend()
        plt.show()  
   
    else:
        print('Thank you for using my calculator!')
        break
       
           
        
