bingo_list = [list(map(int, input().split())) for _ in range(3)]
bingo_bool_list = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]
                  ]

n = int(input())

for i in range(n):
    num = int(input())
    for j in range(3):
        for k in range(3):
            if bingo_list[j][k] == num:
                bingo_bool_list[j][k] = 1

ans = 0
for i in range(3):
    if sum(bingo_bool_list[i]) == 3:
        ans += 1
    if bingo_bool_list[0][i] + bingo_bool_list[1][i] + bingo_bool_list[2][i]:
        ans += 1
if bingo_bool_list[0][0] + bingo_bool_list[1][1] + bingo_bool_list[2][2] == 3:
    ans += 1
if bingo_bool_list[2][0] + bingo_bool_list[1][1] + bingo_bool_list[0][2] == 3:
    ans += 1

if 0 < ans:
    print("Yes")
else:
    print("No")


'''
本書回答
'''
A = []
for _ in range(3):
    row = list(map(int, input().split()))
    A.append(row)

M = [[False, False, False], [False, False, False], [False, False, False]]

N = int(input())


for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print('Yes')
else:
    print('No')