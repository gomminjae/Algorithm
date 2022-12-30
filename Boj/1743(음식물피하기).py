from pydoc import visiblename
import sys 
from collections import deque 
input = sys.stdin.readline

n,m,k = map(int, input().split())

graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]



def bfs(a,b):
    count = 1 
    q = deque() 
    q.append([a,b])
    visited[a][b] = 1 

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    count += 1 
                    visited[nx][ny] = 1 

        
    return count 


for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1


result = 0 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            num = bfs(i,j)
            result = max(result,num)

print(result)
            
            
