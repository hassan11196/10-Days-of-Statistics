# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(arr):
    return sum(arr)/len(arr)
def standard_deviation(arr):
    arr = sorted(arr)
    mean_arr = mean(arr)

    def mean_squared_difference(x):
        return (x - mean_arr) ** 2

    msd_arr = list(map(mean_squared_difference, arr))
    return math.pow((sum(msd_arr)/ len(arr)), 1/2)

t = int(input())
arr = list(map(int, input().split(' ')))

print(standard_deviation(arr))