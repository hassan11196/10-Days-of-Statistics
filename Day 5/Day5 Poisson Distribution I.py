# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def poisson_distribution(lambd, k):
    return (2.718 ** (-lambd)) * ( (lambd ** k)  / (math.factorial(k)))
lambd = float(input())
x = int(input())
ans  = poisson_distribution(lambd, x) 
print('%.3f'%ans)

