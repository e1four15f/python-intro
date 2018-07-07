def C(n, k):
    return C(n-1, k-1) + C(n-1, k) if n > k > 0 else 1

n = int(input())
k = int(input())

print(C(n, k))
