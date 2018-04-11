# EE 381 Project 4
# Hypothesis Testing
# Mark Tan

#Null Hypothesis: System works 50% of the time

import random
import matplotlib.pyplot as plt
import numpy as np

trial_num = 18
success_prob = 0.5
repeat_count = 100

#list to keep track of outcomes in a run
trial = [0]
trial = trial * trial_num

#list to keep track of success frequency
trial_sum = [0]
trial_sum = trial_sum * (trial_num + 1)

for k in range(repeat_count):

    #run bernoulli trials
    for i in range(trial_num):
        r = random.uniform(0,1)
        
        if r < success_prob:   #success
            trial[i] = 1
        else: 			   #failure
            trial[i] = 0
    
    s = sum(trial)
    trial_sum[s] += 1

#create bar chart
hor_axis = np.arange(len(trial_sum))  
plt.bar(hor_axis, trial_sum, align='center', alpha=0.5)
plt.xticks(hor_axis)
plt.xlabel('Number of Successes')
plt.ylabel('Frequency of Success')
plt.title('Binomial Distribution - Type II') 
plt.show()

sig_level = 0.05
min_val = 100
crit_val = 0
prob_sum = 0

for x in range(len(trial_sum),0,-1):

    #find probability for each x-value
    index = x-1
    prob = trial_sum[index] / repeat_count
    print("P({ X =",index,"}) =", format(prob,".2f"))
    
    #find critical value
    prob_sum += prob
    diff = abs(prob_sum - sig_level)
    if diff < min_val:
       min_val = diff   
       crit_val = index

#Expected Critical Value: 13
print("Critical Value is", crit_val)
