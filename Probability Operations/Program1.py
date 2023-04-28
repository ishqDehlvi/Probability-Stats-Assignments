# Aim: Write a python program to calculate Theoretical Probability.
# Also what will be the probability of flipping a coin 10 times and getting head, 6 or more times??

def probability(n, k, p):
    """Calculates the theoretical probability of getting k successes in n trials, with probability p of success."""
    from math import comb
    return comb(n, k) * p**k * (1-p)**(n-k)

# Probability of flipping a coin 10 times and getting a head 6 or more times
p = 0.5 # Probability of getting a head or a tail is 0.5 or 1/2
n = 10 # Number of coin flips
prob = sum(probability(n, k, p) for k in range(6, n+1))
print(f"The probability of flipping a coin {n} times and getting a head 6 or more times is {prob:.4f}")
