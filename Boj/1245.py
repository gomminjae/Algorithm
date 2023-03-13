import sys 
input = sys.stdin.readline
from collections import deque

def bfs(a,b):
    global flag
    q = deque()
    q.append((a,b))
    visited[a][b] = 1 
    
    while q:
        x,y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[x][y] < graph[nx][ny]:
                    flag = False 
                elif graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1 

n,m = map(int, input().split())
graph = [] 
visited = [[0] * m for _ in range(n)]

dx = [0,-1,0,1,1,-1,1,-1]
dy = [1,0,-1,0,1,-1,-1,1]
count = 0 

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and not visited[i][j]:
            flag = True
            bfs(i,j)
            if flag:
               count += 1 
         

print(count)


