n = int(input())

def factorial(n):
    curr = 1;
    for i in range(1, n+1):
        curr *= i
    return curr

print(factorial(n))