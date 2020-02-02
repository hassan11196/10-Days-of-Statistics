# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import statistics

def func(n, X, Y):
    RX = list(sorted(set(X)))
    RY = list(sorted(set(Y)))

    rx = [RX.index(x)+1 for x in X]
    ry = [RY.index(x)+1 for x in Y]
    
    
    di = [ (x - y)**2 for x,y in zip(rx, ry)]
    # print(X)
    # print(Y)
    # print(rx)
    # print(ry)
    # print(di)
    return 1 - ( (6*sum(di))/(n * ((n**2) - 1)))



# total = float(input())
n = int(input())

X = list(map(lambda x: float(x), list(filter(lambda x: True if x != '\r' else False, input().split(' ')))  ))
Y = list(map(lambda x: float(x),input().split(' ')))
PCoeff =  func(n, X, Y) 
print('%.3f'%PCoeff)

