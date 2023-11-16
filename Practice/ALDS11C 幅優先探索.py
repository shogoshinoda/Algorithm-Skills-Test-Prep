from collections import deque
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

visited = [-1]*n

visited[0] = 0
my_deq = deque()
my_deq.append(1)

while len(my_deq) >= 1:
    s = my_deq.popleft()

    for i in l[s-1]:
        if not 0 < i <= n:
            continue
        if visited[i-1] == -1:
            visited[i-1] = visited[s-1] + 1
            my_deq.append(i)

for i in range(n):
    print(str(i+1) + ' ' + str(visited[i]))