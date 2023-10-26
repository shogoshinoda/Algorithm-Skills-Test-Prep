N, Q = map(int, input().split())
fl = [['N' for _ in range(N)] for _ in range(N)]
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        fl[q[1]-1][q[2]-1] = 'Y'
    elif q[0] == 2:
        for i in range(N):
            if fl[i][q[1]-1] == 'Y':
                fl[q[1]-1][i] = 'Y'
    else:
        flc = list(fl[q[1]-1])
        for i in range(N):
            if flc[i] == 'Y':
                for n in range(N):
                    if fl[i][n] == 'Y':
                        fl[q[1]-1][n] = 'Y'

for f in fl:
    print(*f)

