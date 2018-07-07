from math import factorial

n, k = int(input()), int(input())

c = int(factorial(n)/(factorial(k)*factorial(n - k)))
print(c)