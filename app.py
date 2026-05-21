#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:46:10 2026

@author: yuvianasachar
"""
"""Introduction"""


import matplotlib.pyplot as plt
from calculations import initial_investment
from calculations import sip_calculator_at_the_end
from simulations import monthly_portfolio
from simulations import monthly_portfolio_step_up
from allocations import allocationz

#----------------------------------#

print("Welcome to the very basic SIP Calculator for Indian Markets/Mutual Funds")
print('')
print("It just calculates how much money you could make off of your investments based on the amount of risk you're willing to take")
print("")
print("The rates and allocation amounts are based on averages. The calculator doesn't give any real financial advice (yet) ")
print("")

print("Let's get started!")
print("------------------------------------------")

print("-------------------------")

#----------------------------------#

goal=0

""" Creating a dictionary that has set profiles to decide what risk appetite/fund allocation should be based on input the user provides"""

allocations={
    "low": {"Equity": 0.20,
            "Hybrid": 0.30,
            "Debt": 0.50,
            },
    "medium": {"Equity": 0.50,
               "Hybrid": 0.30,
               "Debt": 0.20,
         },
    "high":{ "Equity": 0.70,
            "Hybrid": 0.20,
            "Debt": 0.10,
            }}

#----------------------------------#


    
    
risk_profile, highest_possible_rate, lowest_possible_rate, risk = allocationz(risk)
portfolio=allocations[risk_profile]

#----------------------------------#

print("Based on your risk appetite you have been alloted this portfolio")
print("-------------------------")
for fund_type, percentage in portfolio.items():
        amount=investment_per_month*percentage
        
        print(fund_type,":","₹",amount)



"""Final Outputs"""

month_numbers=timeperiod

print("For a total investment of",'₹',initial_investment(investment_per_month, timeperiod),)
print("If you recieve the lowest possible rate your maturity value at the end of the investing term could be: ₹", sip_calculator_at_the_end(investment_per_month, goal, timeperiod, lowest_possible_rate))
print("If you recieve the highest possible rate your maturity value at the end of the investing term could be: ₹",sip_calculator_at_the_end(investment_per_month, goal, timeperiod, highest_possible_rate))
biggest_maturity=sip_calculator_at_the_end(investment_per_month, goal, timeperiod, highest_possible_rate)
total_invested=initial_investment(investment_per_month, timeperiod)

print("You could earn in interest:",'₹',round(biggest_maturity-total_invested,2))
print("")
print('-------------------------')

print("Would you like to see how your portfolio grows every month visually?")   
choice1=int(input("Enter 1 for yes, enter 2 for no, enter 3 to see with step up SIP of your choice every year: "))
print("")
print('-------------------------')

portfolio_list=monthly_portfolio(timeperiod, investment_per_month, (highest_possible_rate+lowest_possible_rate)/2) 

#----------------------------------#

if choice1==1:
    print("Portfolio growth over time")
    print('')
    for month, value in enumerate(portfolio_list, start=1):
        print("Month", month, ":",'₹', value)
        plt.plot(portfolio_list)
        plt.xlabel("Months")
        plt.ylabel("Growth")
        plt.title("Portfolio growth over time")
        plt.show() 
elif choice1==3:
        s=float(input("Enter, in decimals, by how much you would like to increase your SIP every year: "))
        print("Your projected growth will now be: ", monthly_portfolio_step_up(timeperiod, investment_per_month, (highest_possible_rate+lowest_possible_rate)/2, s))
        choice2=int(input("Would you like to see this graph plotted with the other graph with no SIP? Emter 1 for yes, 2 for no: "))
        if choice2==1:
            portfolio_list_step_up=monthly_portfolio_step_up(timeperiod, investment_per_month, (highest_possible_rate+lowest_possible_rate)/2, s)
            
        plt.plot(portfolio_list_step_up, label='With step up')
        plt.plot(portfolio_list, label='Without step up')
        
        plt.xlabel("Growth")
        plt.ylabel("Months")
        plt.title("Portfolio Growth Over Time")
        plt.legend()
        plt.show()   
else:
    print("Okay! Thank you for using this calculator :3")        

#----------------------------------#


while True:
    print("1. Run calculat")




        
        
