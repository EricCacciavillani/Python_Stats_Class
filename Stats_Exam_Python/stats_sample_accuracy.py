#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:21:05 2017

@author: ericcacciavillani
"""
import math

#------------------------------------
given_percent = 1.711;
error_percentage = 1;
critical_val_z = 1
#------------------------------------


# Make into decimal form
error_percentage = error_percentage/100;
given_percent = given_percent/ 100;

minimum_sample_known = ((critical_val_z**2) * (given_percent * (1-given_percent))) / (error_percentage**2)
minimum_sample_unknown = ((critical_val_z**2) * (.25) / (error_percentage**2))

print("\nThe minimum sample known is", math.ceil(minimum_sample_known))
print("\nThe minimum sample unknown is", math.ceil(minimum_sample_unknown))
