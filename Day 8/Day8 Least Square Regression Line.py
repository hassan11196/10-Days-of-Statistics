# Enter your code here. Read input from STDIN. Print output to STDOUT


def linear_regression(X, Y, n,testx):
    # print(X)
    # print(Y)
    y_ = sum(Y) / n
    x_ = sum(X) / n
    XY = sum([x*y for x,y in zip(X,Y)])
    X2 = sum([x**2 for x in X])
    # print(x_)
    # print(y_)
    # print(X2)
    # print(XY)
    b = ( ((n*XY) - (sum(X)*sum(Y))) / ((n*X2) - (sum(X)**2)))
    # print(b)
    a = y_ - b*x_
    return a + b*testx

X = []
Y = []
n = 5
testx = 80
for x in range(0, n):
    x, y = list(map(lambda x: float(x),input().split(' ')))
    X.append(x)
    Y.append(y)

ans_y =  linear_regression(X, Y, n,testx)
print('%.3f'%ans_y)