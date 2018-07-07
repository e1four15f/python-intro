a, b, c = int(input()), int(input()), int(input())

t = a
t = b if t < b else t
t = c if t < c else t

print(t)