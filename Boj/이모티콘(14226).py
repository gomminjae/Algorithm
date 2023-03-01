from collections import deque
n = int(input())
dist = [[0]* (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  
dist[1][0] = 1
while q:
    s,c = q.popleft()
    if dist[s][s] == 0: 
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == 0:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 > 0 and dist[s-1][c] == 0:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = 0
for i in range(n):
    if dist[n][i] != 0:
        if answer == 0 or answer > dist[n][i]:
            answer = dist[n][i]
print(answer-1)