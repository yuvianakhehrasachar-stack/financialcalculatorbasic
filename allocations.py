#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:01:04 2026

@author: yuvianasachar
"""
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
            low_return=0.11
        return profile, high_return, low_return, risk
     
        
