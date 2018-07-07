a = [int(i) for i in input().split(' ')]

b = set({})
for num in a:
    if num in b:
        print('YES')
    else:
        print('NO')
        b.add(num)


