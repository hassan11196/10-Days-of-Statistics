

def geometric_distribution(p, x):
    return (p) * ((1 - p) ** (x - 1))

a, b = list(map(lambda x:(float(x)), input().split(' ')))
x = int(input())
p = a / b
ans  = geometric_distribution(p, x) 
print('%.3f'%ans)

