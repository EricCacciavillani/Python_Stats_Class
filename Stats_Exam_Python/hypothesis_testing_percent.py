#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:08:24 2017

@author: ericcacciavillani
"""
import math
import scipy.stats as st

sample_amount = 30
superset_amount = 50

percent_claim = .5
significance_level = .05

#right tailed --Greater than more than
#left tailed -- Less than
#two tailed -- is/ equal to 
tailed_type = "right tailed"

#------------------------------------

### Ensures percent format
if percent_claim >= 1:
    percent_claim = percent_claim / 100
    
if significance_level >= 1:
    significance_level = significance_level / 100

#------------------------------------

# Grab only the first word
tailed_type = tailed_type.split(" ")[0].lower()

p_hat = sample_amount / superset_amount;

test_statistic = (p_hat - percent_claim) / math.sqrt(((percent_claim) * (1 - percent_claim))/superset_amount)


p_value = 0;
critical_value = 0;

test_statistic = round(test_statistic,4)
p_hat = round(p_hat,3)

print("\nP hat is",p_hat)
print("Test statistic is",test_statistic)



if test_statistic == 1.645 or test_statistic == 1.96 or test_statistic == 2.575:
     p_value = round(st.norm.cdf(test_statistic),3)
else:
     p_value = round(st.norm.cdf(test_statistic),4)





if tailed_type == "right":
    p_value = 1 - p_value
    
elif tailed_type == "left":
    ### Do nothing!
    0;
    
elif tailed_type == "two":

    if test_statistic < 0:
       p_value =  p_value * 2;
    else:
        p_value = (1 - p_value) * 2


print ("p value = ", p_value)

print ("\nThe critical value is ", round(st.norm.ppf(1-significance_level),3))

print ("WARNING! MAKE SURE THE P_Value IS NOT A SPECIAL VAL! (EXAMPLE .90)")

print("#############################################################################\n")


if significance_level < p_value:
    
    print ("We fail to reject the null or H^0")
    
    if (tailed_type == "right" or tailed_type == "left"):
        print("There is not enough data to support the claim that...")
        
    else:
        print("There is not enough data to justify reaction of the claim that...")
        
    
else:
    print("We must reject null or H^0")
    
    if (tailed_type == "right" or tailed_type == "left"):
        
        print("The data supports the claim that...")
        
    else:
        print("There is enough data to justify reaction of the claim that...")