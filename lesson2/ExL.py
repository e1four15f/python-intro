a, b, c = int(input()), int(input()), int(input())

a, b = (b, a) if a > b else (a, b)
a, c = (c, a) if a > c else (a, c)
b, c = (c, b) if b > c else (b, c)

print(a, b, c)

