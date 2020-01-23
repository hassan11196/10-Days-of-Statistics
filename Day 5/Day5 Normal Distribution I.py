# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def normal_density_function(mean, sd, x):
    # ans = (((2.718) ** (-1* ( ((q - mean)**2)/(2*(sd ** 2)  ))) /(sd * ((2 * 3.14159)**(1/2))))

    return ( (math.e ** (-1/2 * ((x - mean)/sd) ** 2)) / (sd * math.pow(2*math.pi, 0.5)) )

def cumulative_prob(mean, sd, x):
    return 1/2 * (1 + math.erf( (x-mean)/(sd * (2**0.5)) ))


def normal_distribution(mean, sd, q,  low, high):
    ans1 = cumulative_prob(mean, sd, q)
    ans2 = cumulative_prob(mean, sd, high) -cumulative_prob(mean, sd, low)


    return (ans1, ans2)
mean,sd = list(map(float, input().split(' ')))
q = float(input())
low,high = list(map(float, input().split(' ')))
ans1, ans2  = normal_distribution(mean, sd, q,  low, high) 
print('%.3f'%ans1)
print('%.3f'%ans2)
