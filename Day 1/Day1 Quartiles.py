# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def quartile(arr):
    arr = sorted(arr)
    if len(arr)%2 == 0:
        q1_arr = arr[:round(len(arr)/2)]
        q3_arr = arr[round(len(arr)/2):]
    else:    
        index = median_index(arr)
        q1_arr = arr[:index+1]
        q3_arr = arr[index+2:]

    q1 = round(median(q1_arr))
    q2 = round(median(arr))
    q3 = round(median(q3_arr))

    return (q1, q2, q3)


def median(arr):
    arr = sorted(arr)
    if (len(arr)%2 == 0):
        return (arr[int(len(arr)/2)-1] +arr[int(len(arr)/2) ])/2
    else:
        return arr[int(len(arr)/2)] 

def median_index(arr):
    arr = sorted(arr)
    if (len(arr)%2 == 0):
        return int(len(arr)/2)
    else:
        return int(len(arr)/2) -1 

t = int(input())
arr = list(map(int, input().split(' ')))

q = quartile(arr)
for quartile in q:
    print(quartile)
