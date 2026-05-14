#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:46:10 2026

@author: yuvianasachar
"""
"""Introduction"""


print("Welcome to the very basic SIP Calculator for Indian Markets/Mutual Funds")
print('')
print("It just calculates how much money you could make off of your investments based on the amount of risk you're willing to take")
print("")
print("The rates and allocation amounts are based on averages. The calculator doesn't give any real financial advice (yet) ")
print("")
print("Let's get started!")
print("------------------------------------------")
investment_per_month=float(input("How much would you like to invest monthly (in rupees)?: "))
# goal=float(input("Great! What is your financial goal? Enter the amount of money you would like to recieve at the end of the investing term: "))
timeperiod=int(input("Cool! Enter the time period you have for this investment in MONTHS: "))
risk=int(input("Lovely! And from a scale of 1-10, how much risk are you willing to take with 1 being no risk at all and 10 being as risky as it gets?"))
print("-------------------------")


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

def allocationz(risk):

    if risk in range(0,4):
        profile="low"
        high_return=0.105
        low_return=0.085
    elif risk in range (4,7):
        profile="medium"
        high_return=0.125
        low_return=0.100
    else:
        profile="high"
        high_return=0.135
        low_return=00.11
    return profile, high_return, low_return

risk_profile, highest_possible_rate, lowest_possible_rate = allocationz(risk)
portfolio=allocations[risk_profile]

#----------------------------------#
print("Based on your risk appetite you have been alloted this portfolio")
print("-------------------------")
for fund_type, percentage in portfolio.items():
        amount=investment_per_month*percentage
        
        print(fund_type,":", amount)

#----------------------------------#

def sip_calculator(investment_per_month,goal,timeperiod,rate):
    """ Using these values, we cab calculate the basic SIP amount
    For the lowest possible rate from portfolio allocation"""
    monthly_rate=rate/12
    maturity_value=float(investment_per_month*(((1+monthly_rate)**timeperiod-1)/monthly_rate)*(1+monthly_rate))
    return round(maturity_value,2)
    return maturity_value

#----------------------------------#

def initial_investment(investment_per_month,timeperiod):
    total_investment=investment_per_month*timeperiod
    return total_investment

#----------------------------------#
   
"""Final Outputs"""
  
print("For a total investment of",initial_investment(investment_per_month, timeperiod),"rupees")
print("If you recieve the lowest possible rate your maturity value at the end of the investing term could be:",sip_calculator(investment_per_month, goal, timeperiod,lowest_possible_rate))
print("If you recieve the highest possible rate your maturity value at the end of the investing term could be:",sip_calculator(investment_per_month, goal, timeperiod, highest_possible_rate))
biggest_maturity=sip_calculator(investment_per_month, goal, timeperiod, highest_possible_rate)
total_invested=initial_investment(investment_per_month, timeperiod)

print("You could earn in interest:",round(biggest_maturity-total_invested,2))