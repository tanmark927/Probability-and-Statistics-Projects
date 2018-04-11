# Calculate Bayes probabilities

#Given values
sample_size = 5

#Probability of having disease
prob_c = [0.0001, 0.001, 0.001, 0.0001, 0.001]

#Probability of presence of disease with diagnostic
prob_b_given_c = [0.9,0.9,0.9,0.95,0.95]

#Probability of lack of disease with diagnostic
prob_b_given_cprime = [0.001, 0.001, 0.01, 0.001, 0.01]

#Values to calculate
prob_b = [0] * sample_size
prob_c_given_b = [0] * sample_size

for i in range(sample_size):
    #needed to solve Bayes rule
    prob_b[i] = prob_b_given_c[i] + prob_b_given_cprime[i]
    
    #Bayes rule
    prob_c_given_b[i] = prob_b_given_c[i] * prob_c[i] / prob_b[i]

#Solution value
print(prob_c_given_b)