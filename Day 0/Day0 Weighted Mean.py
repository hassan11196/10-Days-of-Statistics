def weighted_mean(val, weight):
    products = []
    for v,w in zip(val, weight):
        products.append( v * w )
    return sum(products) / sum(weight)
        


# Enter your code here. Read input from STDIN. Print output to STDOUT
val = int(input())
val = list(map(int, input().split()))
weight = list(map(int, input().split()))

print("%.1f"%weighted_mean(val,weight))