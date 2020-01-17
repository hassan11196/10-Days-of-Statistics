# Enter your code here. Read input from STDIN. Print output to STDOUT

def mean(arr):
    return sum(arr)/len(arr)

def median(arr):
    arr = sorted(arr)
    if (len(arr)%2 == 0):
        return (arr[int(len(arr)/2) - 1] +arr[int(len(arr)/2) ])/2
    else:
        return arr[int(len(arr)/2) - 1] 
def mode(arr):
    dic = {}
    for x in arr:
        try:
            dic[x] += 1
        except KeyError as e:
            dic[x] = 1
    max_val = 0
    max_key = 0
    for x,y in dic.items():
        if y > max_val:
            max_val = y
            max_key = x
        elif y == max_val:
            max_key = max_key if max_key < x else x
            max_val = y
    
    return max_key



t = int(input())
arr = input().split(' ')
arr = list(map(lambda x:int(x),arr))

print(mean(arr))
print(median(arr))
print(mode(arr))
