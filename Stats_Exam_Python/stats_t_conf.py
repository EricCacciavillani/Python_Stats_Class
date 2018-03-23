#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:56:54 2017

@author: ericcacciavillani
"""
import math

#------------------------------------
given_mean = 6.2
critical_val = 2.575
selected_amount = 30
standard_devation = 1.25
#------------------------------------

margin_of_error = critical_val * (standard_devation/math.sqrt(selected_amount))

margin_of_error = round(margin_of_error,5)

upper_limit = given_mean + margin_of_error;
lower_limit = given_mean - margin_of_error;

print("\nMake sure to get the t val you subtracted 1 to the selected amount!!!\n")
print ("Margin of error for t is",margin_of_error)

print("\nCheck the limits manually after rounding!!!")

print("\nUpper Limit", upper_limit)
print("Lower Limit", lower_limit)