# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cumulative_prob(mean, sd, x):
    return 1/2 * (1 + math.erf( (x-mean)/(sd * (2**0.5)) ))


def func(total, n, mean, sd):
    mean2 = n * mean
    sd2 = (n ** 0.5) * sd

    return cumulative_prob(mean2, sd2, total)
total = float(input())
n = float(input())
mean = float(input())
sd = float(input())
ans  =  func(total, n, mean, sd) 
print('%.4f'%ans)

