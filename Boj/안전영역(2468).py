import sys 
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(x,y,k):
    queue = deque() 
    queue.append((x,y))
    
    visited[x][y] = 1 
    
    while queue:
        x,y = queue.popleft() 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= k and visited[nx][ny] == 0:
                    visited[nx][ny] = 1 
                    queue.append((nx,ny))
    


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
min_value = min(map(min,graph))
max_value = max(map(max,graph))

max_k = min_value

for k in range(min_value, max_value+1):
    visited = [[0] * n for _ in range(n)]
    count = 0 
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= k and visited[i][j] == 0:
                bfs(i,j,k)
                count += 1 
    if count > max_k:
        max_k = count 
            

print(max_k)