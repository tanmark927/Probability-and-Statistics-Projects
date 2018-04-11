# EE 381 Project 4
# Hypothesis Testing - Type II Error
# Mark Tan

#Alt Hypothesis: System works more than 50% of the time

import random
import matplotlib.pyplot as plt
import numpy as np

trial_num = 18
crit_val = 13 #value based on result in Proj 4 Part 1
repeat_count = 100

start = 0.55
end = 1.00
increment = 0.05

prob_values = [0]
prob_values = prob_values * 10

power_vals = [0]
power_vals = power_vals * 10

for success_prob in np.arange(start,end+increment,increment):
    prob_values[int((success_prob - start)/increment)] = success_prob
	
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
            else: 			  #failure
                trial[i] = 0
    
        s = sum(trial)
        trial_sum[s] += 1    
    
    print("Probability of Success:",success_prob)    
    
    #create bar chart
    hor_axis = np.arange(len(trial_sum))  
    plt.bar(hor_axis, trial_sum, align='center', alpha=0.5)
    plt.xticks(hor_axis)
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency of Success')
    plt.title('Binomial Distribution - Type II')
    plt.show()    
    
    prob_sum = 0
    for z in range(crit_val):
        #find probability for each x-value
        prob = trial_sum[z] / repeat_count
        print("P({ X =",z,"}) =", format(prob,".2f"))
        prob_sum += prob
    
    print("Beta value:",format(prob_sum,".2f"))
    power = 1 - prob_sum
    print("Power value:",format(power,".2f"))
    power_vals[int((success_prob - start)/increment)] = power
    print(" ")
				
plt.plot(prob_values, power_vals)
plt.title('The Power of the Test')
plt.xlabel('Success Probabilities')
plt.ylabel('Power Levels')
plt.show()
