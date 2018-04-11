# EE 381 Project 3 Part 3
# Binomial Distribution Using Frequency Simulation
# EE 381 - Mark Tan

import random
import matplotlib.pyplot as plt
import numpy as np

E = 0 #average accumulator
success_prob = float(input("Type in the probability of success: "))
trial_num = int(input("Type in the number of trials: "))
low_end = int(input("Type in the lowest number of successes for this trial: "))
high_end = int(input("Type in the highest number of successes for this trial: "))

while True:
    success_count = int(input("Type in the number of successes: "))
    if success_count >= low_end | success_count <= high_end:
        #correctly constrained
        break
    else:
        #not constrained
        continue

repeat_count = 100

trial = [0]               #single entry list
trial = trial * trial_num #increase list size to trial_num

trial_sum = [0,0,0,0,0,0] #list to keep track of success frequency

j = 0                     #success trial count

for k in range(repeat_count):
    
    for i in range(trial_num): #bernoulli trials
        r = random.uniform(0,1)
        
        if r < success_prob:
            trial[i] = 1       #success
        else:
            trial[i] = 0       #failure
    
    s = sum(trial)
    trial_sum[s] += 1
    E = E + s
    
    if s == success_count:
        j = j + 1

print(' ')

prob = j / repeat_count
print("The probability of three successes in five trials is", format(prob,".4f"))

avg = E / repeat_count
print("The average value of success is", avg)

option = str(input("Would you like to see a bar chart of the results? "))
if(option.lower() == "yes"):
    objects = ('0','1', '2', '3', '4', '5')
    hor_axis = np.arange(len(objects))  
    plt.bar(hor_axis, trial_sum, align='center', alpha=0.5)
    plt.xticks(hor_axis, objects)
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency of Success')
    plt.title('Binomial Distribution Using Frequency Simulation') 
    plt.show()
