
import sys 
from collections import deque 
input = sys.stdin.readline

n = int(input())
graph = [] 

for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a,b,size):
    q = deque() 
    q.append((a,b))
    result = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1 
    temp = [] 
    
    while q:
        x,y = q.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1 
                    result[nx][ny] = result[x][y] + 1 

                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp.append((nx,ny,result[nx][ny]))
    
    return sorted(temp,key=lambda x: (x[2],x[1],x[0]), reverse=True)
    
count = 0 
shark_size = 2 
time = 0 
#상어 위치 찾기 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x,y = i,j

while True:
    ans = bfs(x,y,shark_size)
    print(ans)

    if len(ans) == 0:
        break 

    shark_x, shark_y, distance = ans.pop() 
    
    time += distance
    graph[x][y] = 0 
    graph[shark_x][shark_y] = 0

    x,y = shark_x, shark_y
    count += 1 

    if count == shark_size:
        shark_size += 1 
        count = 0 

print(time)


