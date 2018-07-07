x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if ((y2 - 2 == y1 or y2 + 2 == y1) and (x2 - 1 == x1 or x2 + 1 == x1)
        or (x2 - 2 == x1 or x2 + 2 == x1) and (y2 - 1 == y1 or y2 + 1 == y1)):
    print('YES')
else:
    print('NO')

