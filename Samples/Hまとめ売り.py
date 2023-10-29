N = int(input())
C = list(map(int, input().split()))
Q = int(input())
ans = 0
elist = list()
for i in range(1, N+1):
    if (i % 2 == 1):
        elist.append(i-1)
for _ in range(Q):
    S = list(map(int, input().split()))
    if (S[0] == 1):
        x = S[1] - 1
        a = S[2]
        if (C[x] >= a):
            C[x] -= a
            ans += a
    elif (S[0] == 2):
        a = S[1]
        b = True
        for i in elist:
            if not (C[i] >= a):
                b = False
        if (b):
            for i in elist:
                C[i] -= a
                ans += a
    else:
        a = S[1]
        b = True
        for i in range(N):
            if not (C[i] >= a):
                b = False
        if (b):
            for i in range(N):
                C[i] -= a
                ans += a

print(ans)