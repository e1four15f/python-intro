import math

a = int(input())

if math.fmod(a, 4) == 0 and math.fmod(a, 100) != 0 or math.fmod(a, 400) == 0:
    print('YES')
else:
    print('NO')