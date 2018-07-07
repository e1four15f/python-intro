a = input()

first_index = a.find('h')
last_index = len(a) - a[::-1].find('h')
b = a[first_index:last_index]

print(a[:first_index] + b[::-1] + a[last_index:])

