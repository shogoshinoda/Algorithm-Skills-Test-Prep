from collections import deque

visited = []
for i in range(N):
    visited.append(False)

Q = deque
Q.append(s)
visited[s] = True

while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        if not visited[j]:
            visited[j] = True
            Q.append(j)