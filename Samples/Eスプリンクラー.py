N, M, Q = map(int, input().split())
mp = [list() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    mp[u-1].append(v-1)
    mp[v-1].append(u-1)
cl = list(map(int, input().split()))

ql = [list(map(int, input().split())) for _ in range(Q)]
for q in ql:
    print(cl[q[1]-1])
    if q[0] == 1:
        for i in mp[q[1]-1]:
            cl[i] = cl[q[1]-1]
    else:
        cl[q[1]-1] = q[2]

