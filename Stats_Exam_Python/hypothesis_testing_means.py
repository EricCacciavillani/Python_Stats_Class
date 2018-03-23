#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:23:49 2017

@author: ericcacciavillani
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:08:24 2017

@author: ericcacciavillani
"""
import math
import scipy.stats as st


# if they don't give the overall mean then it is 0
overall_mean = 50502;

sample_amount = 50;
sample_mean = 52776;
sample_std_dev = 5785;

significance_level = 0.01;

# MAKE SURE TO CHANGE ME!!!!!!!
#----------------------------------
#right tailed --Greater than more than
#left tailed -- Less than
#two tailed -- is/ equal to

tailed_type = "two tailed"



if significance_level >= 1:
    significance_level = significance_level/100;

# Grab only the first word
tailed_type = tailed_type.split(" ")[0].lower()

test_statistic = (sample_mean - overall_mean) / (sample_std_dev / math.sqrt(sample_amount))
test_statistic = round(test_statistic,2)

# defining away from user input area
critical_value = 0;

print("\n")

"""
if tailed_type == "two":
    print("Claim: U != ",overall_mean)
    print("H^1: U =",overall_mean)
    print("H^0: U !=",overall_mean)

elif tailed_type == "left":
    print("Claim: U < ",overall_mean)
    print("H^1: U =",overall_mean)
    print("H^0: U < ",overall_mean)

elif tailed_type == "right":
    print("Claim: U > ",overall_mean)
    print("H^1: U =",overall_mean)
    print("H^0: U > ",overall_mean)

"""

print("\nTest_Statistic: ", test_statistic)

if tailed_type == "left":
    critical_value = st.t.ppf(significance_level, sample_amount-1) 
elif tailed_type == "right":
    critical_value =  (st.t.ppf(significance_level, sample_amount-1))*-1        
elif tailed_type == "two":
    critical_value = (st.t.ppf(significance_level/2, sample_amount-1))*-1 
else:
    print("Inavlid tailed_type: ",tailed_type)
    
critical_value = round(critical_value,3)

if(tailed_type != "two"):
    print("Critical value: ", critical_value)
else:
    print("Critical value: +-", critical_value)

print("------------------------------------------")

if (tailed_type =="left" and test_statistic > critical_value) or (tailed_type =="right" and test_statistic < critical_value) or (tailed_type == "two" and test_statistic < critical_value and test_statistic > (critical_value * -1)):
    
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





