
import sys 
from collections import deque 
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [] 

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(n):
    graph.append(list(map(int, input().split())))


result = []
def bfs():
    q = deque() 
    q.append((0,0))
    visited[0][0] = 1 

    count = 0 


    while q:
        x,y = q.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1 

                    q.append((nx,ny))
                else:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1 
                    count += 1
    result.append(count)
    return count


hours = 0 


while True:
    hours += 1

    visited = [[0]*m for _ in range(n)]

    count = bfs() 

    if count == 0:
        break


print(hours-1)
print(result[-2])
