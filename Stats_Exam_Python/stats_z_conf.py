#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:41:13 2017

@author: ericcacciavillani
"""
import math

#------------------------------------
given_val = 90
sample_size = 100
critical_val = 1.96
#------------------------------------



point_estimate = given_val/ sample_size;
q_of_p = 1 - point_estimate;

margin_of_error = critical_val * math.sqrt(point_estimate * q_of_p / sample_size)


point_estimate = round (point_estimate,5)
margin_of_error = round (margin_of_error,5)

upper_limit = point_estimate + margin_of_error
lower_limit = point_estimate - margin_of_error

print("\nPoint Estimate: ", point_estimate)
print("Critical Val Z:",critical_val)
print("Margin of Error: ", margin_of_error)

print("\nCheck the limits manually after rounding!!!")

print("\nUpper Limit", upper_limit)
print("Lower Limit", lower_limit)

