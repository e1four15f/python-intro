from math import factorial as fact

n = int(input())

sum = 0;
for i in range(1, n+1):
    sum += fact(i)

print(sum)
