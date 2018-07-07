n = int(input())
a, b, c = 0, 0, 0

while n >= 35:
    c += 1
    n = n - 60 if n >= 60 else 0

while n >= 9:
    b += 1
    n = n - 10 if n >= 10 else 0

a = n

print(a, b, c)
