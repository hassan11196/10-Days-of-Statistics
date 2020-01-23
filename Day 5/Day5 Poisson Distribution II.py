# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def poisson_distribution(l1, l2):
    ans1 = 160 + (40*(l1 + (l1)**2))
    ans2 = 128 + (40*(l2 + (l2)**2))
    return (ans1, ans2)
lambd1,lambd2 = list(map(float, input().split(' ')))
ans1, ans2  = poisson_distribution(lambd1, lambd2) 
print('%.3f'%ans1)
print('%.3f'%ans2)
