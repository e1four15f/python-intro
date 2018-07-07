def pow(a, n):
    return a*pow(a, n-1) if n > 0 else 1

a = float(input())
n = int(input())

print(pow(a, n))