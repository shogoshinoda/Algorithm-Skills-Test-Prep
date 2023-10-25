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