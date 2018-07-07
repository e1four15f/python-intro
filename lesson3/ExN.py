N = int(input())

M = []
for i in range(N):
    M.append(set({}))
    Mi = int(input())
    for j in range(Mi):
        M[i].add(input())

M_all = set({})
M_intersection = M[0].copy()
for i in range(N):
    M_all.update(M[i])
    M_intersection.intersection_update(M[i])

print(len(M_intersection))
print('\n'.join(str(i) for i in M_intersection))

print(len(M_all))
print('\n'.join(str(i) for i in M_all))
