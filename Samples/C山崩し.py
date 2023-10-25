N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N-2, -1, -1):
    for j in range(2 * N -1):
        if S[i][j] != '.':
            if j == 0:
                if S[i+1][j] == 'X' or S[i+1][j+1] == 'X':
                    S[i][j] = 'X'
            elif j == 2 * N - 2:
                if S[i+1][j-1] == 'X' or S[i+1][j] == 'X':
                    S[i][j] = 'X'
            else:
                if S[i+1][j-1] == 'X' or S[i+1][j] == 'X' or S[i+1][j+1] == 'X':
                    S[i][j] = 'X'


for i in range(N):
    print(''.join(S[i]))                
