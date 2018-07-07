def IsPrime(x):
    d = 2
    while d * d <= x and x % d != 0:
        d += 1
    return d * d > x

x = int(input())

print('YES' if IsPrime(x) else 'NO')