# EE 381 Project 3 Part 1 and 2
# Binomial Distribution
# EE 381 - Mark Tan

import random

E = 0 #average accumulator
trial_num = 5
success_prob = 0.7
success_count = 3
repeat_count = 100

trial = [0] # single entry list
trial = trial * trial_num # increase list size to trial_num

j = 0 #accumulating variable

for k in range(repeat_count):
    
    #bernoulli trials    
    for i in range(trial_num):
        r = random.uniform(0,1)
        
        if r < success_prob:
            trial[i] = 1 # success
        else:
            trial[i] = 0 # failure
    
    #for Part 2
    s = sum(trial)        
    E = E + s
    
    #for Part 1
    if s == success_count:
        j = j + 1

#for Part 1
#Exercise 1: P({X = x}) = nCx p**x q**(n-x)
#P({X = 3}) = 5C3 0.7^3 0.3^2
#P({X = 3}) = 10 * 0.343 * 0.09
#-----Expected: P({X = 3}) = 0.3087-----
prob = j / repeat_count
print("Part 1: The probability of three successes in five trials is", format(prob,".4f"))

#for Part 2
#Exercise 2: mu = np
#mu = 5 * 0.7
#-----Expected: mu = 3.5-----
avg = E / repeat_count
print("Part 2: The average value of success is", avg)