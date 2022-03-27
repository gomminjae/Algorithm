import sys 
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(i,j):
    queue = deque() 
    queue.append((i,j))
    graph[i][j] = 1 
    count = 1
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = 1 
                count += 1 
    
    return count 

m,n,k = map(int, input().split())
graph = [list(0 for _ in range(n)) for _ in range(m)]

for _ in range(k):
    a,b,c,d = map(int, input().split())
    
    for i in range(m-d,m-b):
        for j in range(a,c):
            graph[i][j] = 1 
            

result = 0
maps = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            maps.append(bfs(i,j))
            result += 1 

print(result)
maps.sort() 
print(*maps)