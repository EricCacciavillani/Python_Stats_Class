#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:05:59 2017

@author: ericcacciavillani

"""

import scipy.stats as ss

n = 15          # Number of total bets
p = .4          # Probability of event
max_sbets = 3   # Maximum number of successful bets

hh = ss.binom(n, p)

total_p = 0
for k in range(1, max_sbets + 1):  # DO NOT FORGET THAT THE LAST INDEX IS NOT USED
    total_p += hh.pmf(k)
    
print(total_p)
