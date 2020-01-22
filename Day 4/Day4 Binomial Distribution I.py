# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
NUMBER_TRIALS = 6
NUMBER_SUCCESS = 3

def nCr(n,r):
    f = math.factorial
    return (f(n)) / ((f(n - r))*f(r))

def binomial_probabilty(n, x, p , q):
    return nCr(n, x) * (p ** x) * ((q) ** (n-x))


def binomial_distribution(a, b):
    sample = a + b
    prob_a = a / sample
    prob_b = b / sample

    return binomial_probabilty(NUMBER_TRIALS,NUMBER_SUCCESS, prob_a, prob_b) + binomial_probabilty(NUMBER_TRIALS, NUMBER_SUCCESS + 1, prob_a, prob_b) + binomial_probabilty(NUMBER_TRIALS, NUMBER_SUCCESS + 2, prob_a, prob_b) + binomial_probabilty(NUMBER_TRIALS, NUMBER_SUCCESS + 3, prob_a, prob_b)



boy, girl = list(map(lambda x:(float(x)), input().split(' ')))
ans = binomial_distribution(boy, girl) 
print('%.3f'%ans)
