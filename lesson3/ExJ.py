a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]

print(len(set(a).intersection(set(b))))