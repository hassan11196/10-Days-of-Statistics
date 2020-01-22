# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
NUMBER_TRIALS = 6
NUMBER_SUCCESS = 3

def nCr(n,r):
    f = math.factorial
    return (f(n)) / ((f(n - r))*f(r))

def binomial_probabilty(n, x, p , q):
    return nCr(n, x) * (p ** x) * ((q) ** (n-x))


def binomial_distribution(p, n):
    p = p / 100

    ans1 = binomial_probabilty(n, 0, p, 1-p) + binomial_probabilty(n, 1, p, 1-p) + binomial_probabilty(n, 2, p, 1-p)
    ans2 = binomial_probabilty(n, 2, p, 1-p) + binomial_probabilty(n, 3, p, 1-p) + binomial_probabilty(n, 4, p, 1-p) + binomial_probabilty(n, 5, p, 1-p) + binomial_probabilty(n, 6, p, 1-p) + binomial_probabilty(n, 7, p, 1-p) + binomial_probabilty(n, 8, p, 1-p) + binomial_probabilty(n, 9, p, 1-p) + binomial_probabilty(n, 10, p, 1-p) 

    return (ans1, ans2)

p, n = list(map(lambda x:(float(x)), input().split(' ')))
ans1, ans2  = binomial_distribution(p, n) 
print('%.3f'%ans1)
print('%.3f'%ans2)
