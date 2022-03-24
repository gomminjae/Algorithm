import sys 
from collections import deque 

input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
n = int(input())

def bfs(x,y,z,g):
     queue = deque() 
     queue.append((x,y))
     graph[x][y] = 1 

     
     while queue:
         px,py = queue.popleft() 
         if px == z and py == g:
             print(graph[z][g]-1)
             return 
         for i in range(8):
             nx = px + dx[i]
             ny = py + dy[i]

             if 0 <= nx < k and 0 <= ny < k and graph[nx][ny] == 0:
                 queue.append((nx,ny))
                 graph[nx][ny] = graph[px][py] + 1  
         
     


for _ in range(n):
    k = int(input())
    x,y = map(int, input().split())
    z,g = map(int, input().split())
    graph = [[0] * k for _ in range(k)]

    bfs(x,y,z,g)


