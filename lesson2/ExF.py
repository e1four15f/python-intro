n, m, k = int(input()), int(input()), int(input()) #[int(i) for i in input().split(',')]

if (k % m == 0 or k % n == 0) and n*m >= k:
    print('YES')
else:
    print('NO')
