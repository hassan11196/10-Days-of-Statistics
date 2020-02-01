# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def func(n, mean, sd, p, z):
    mean2 = mean * n
    sd2 =  sd * pow(n, 0.5)
    A = ((z * sd2) + mean2) / n
    B = ((-1 * z * sd2) + mean2) / n
    

    return (A, B)
# total = float(input())
n = float(input())
mean = float(input())
sd = float(input())
p = float(input()) 
z = float(input())
ans1,ans2   =  func(n, mean, sd, p, z) 
print('%.2f'%ans1)
print('%.2f'%ans2)
