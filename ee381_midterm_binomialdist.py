# Binomial Distribution Problem
# Home Ownership
# EE 381 - Mark Tan

import random

house_count = 500
ownership_rate = .659
success_count = 340

trial = [0] #initialize trial list
trial = trial * house_count # increase array size to house_count

j = 0 #accumulating variable

#repetition count
for k in range(100000):

    #number of bernoulli trials    
    for i in range(house_count):
        variable = random.uniform(0,1)

        if variable < ownership_rate:
            #if household lives in a home they own
            trial[i] = 1
        else:
            #if household does not live in a home they own
            trial[i] = 0
    
    #add the successes
    s = sum(trial)

    # increment for probability    
    if s == success_count:
        j = j + 1
prob = j / 100000
print("The probability 340 households live in homes they own is",format(prob,".4f"))