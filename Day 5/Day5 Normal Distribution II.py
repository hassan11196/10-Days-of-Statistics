# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def normal_density_function(mean, sd, x):
    # ans = (((2.718) ** (-1* ( ((q - mean)**2)/(2*(sd ** 2)  ))) /(sd * ((2 * 3.14159)**(1/2))))

    return ( (math.e ** (-1/2 * ((x - mean)/sd) ** 2)) / (sd * math.pow(2*math.pi, 0.5)) )

def cumulative_prob(mean, sd, x):
    return 1/2 * (1 + math.erf( (x-mean)/(sd * (2**0.5)) ))


def normal_distribution(mean, sd, q,  threshold):
    ans1 = 1 - cumulative_prob(mean, sd, q)
    ans2 = 1 - cumulative_prob(mean, sd, threshold) 
    ans3 = cumulative_prob(mean, sd, threshold)

    return ((ans1*(sd**2)), (ans2*(sd**2)) , (ans3*(sd**2)) )
mean,sd = list(map(float, input().split(' ')))
q = float(input())
threshold = float(input())
ans1, ans2, ans3  = normal_distribution(mean, sd, q,  threshold) 
print('%.2f'%ans1)
print('%.2f'%ans2)
print('%.2f'%ans3)
