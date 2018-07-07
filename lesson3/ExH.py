a = [int(i) for i in input().split(' ')]

#min_index = a.index(min(a))
#max_index = a.index(max(a))
#a[min_index], a[max_index] = a[max_index], a[min_index]

max, min = max(a), min(a)
for i in range(len(a)):
    if a[i] == min:
        a[i] = max
    elif a[i] == max:
        a[i] = min

print(' '.join(str(i) for i in a))