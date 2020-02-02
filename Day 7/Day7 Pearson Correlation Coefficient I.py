# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import statistics

def func(n, X, Y):
     
    X_mean = statistics.mean(X)
    Y_mean = statistics.mean(Y)

    x_sd = math.sqrt((sum([(x - X_mean)**2 for x in X])) / (n))
    y_sd = math.sqrt((sum([(y - Y_mean)**2 for y in Y])) / (n))
    # print(X)
    # print(Y)
    # print(x_sd)
    # print(y_sd)
    # print(X_mean)
    # print(Y_mean)

    return sum([ (X[i]-X_mean)*(Y[i]-Y_mean) for i in range(0, n)]) / (n * x_sd * y_sd)

# total = float(input())
n = int(input())

X = list(map(lambda x: float(x), list(filter(lambda x: True if x != '\r' else False, input().split(' ')))  ))
Y = list(map(lambda x: float(x),input().split(' ')))
PCoeff =  func(n, X, Y) 
print('%.3f'%PCoeff)

