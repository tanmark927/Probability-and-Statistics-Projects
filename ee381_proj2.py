# Simulate Bernoulli trials

import random

trial_num = int(input("How many trials would you like to simulate? "))
success_prob = float(input("What is the desired probability of success? "))
success_count = int(input("How many successes should there be per trial? "))
repeat_count = int(input("How many repetitions? "))

trial = [0] # single entry list
trial = trial * trial_num # increase list size to trial_num

j = 0 #accumulating variable

#repeat the trials
for k in range(repeat_count):

	# bernoulli trials
    for i in range(trial_num):
        r = random.uniform(0,1)
        
        if r < success_prob:
            trial[i] = 1 # heads
        else:
            trial[i] = 0 # tails
    
    s = sum(trial)
    
    # increment for probability    
    if s == success_count:
        j = j + 1
        
prob = j / repeat_count
print("The probability of a heads is",prob)