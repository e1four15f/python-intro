a, b = int(input()), int(input())

if a != 0 and b % a == 0:
    print(int(-b/a))
elif a == 0 and b == 0:
    print('INF')
else:
    print('NO')
