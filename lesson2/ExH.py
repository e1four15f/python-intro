n = int(input())

if n in range(11, 15):
    print(n, 'korov')
else:
    mod = n % 10
    if mod == 0 or mod in range(5, 10):
        print(n, 'korov')
    elif mod == 1:
        print(n, 'korova')
    elif mod in range(2, 5):
        print(n, 'korovy')