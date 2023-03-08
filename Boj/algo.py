import sys 
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph = [] 
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

visited = [[0] * m for _ in range(n)]
distance = [[-1]*m for _ in range(n)]

def bfs(a,b):
    q = deque() 
    q.append((a,b))
    visited[a][b] = 1 
    distance[a][b] = 0 
    
    while q:
        x,y = q.popleft()
        for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
        
           if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
               if graph[nx][ny] != 0:
                   distance[nx][ny] = distance[x][y] + 1 
                   q.append((nx,ny))
                   visited[nx][ny] = 1 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            distance[i][j] = 0


bfs(0,0)

for i in range(n):
    print(*distance[i])