import sys
input = sys.stdin.readline
from collections import deque

dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    q = deque()
    q.append((sz,sx,sy))

    while q:
        z,x,y = q.popleft() 

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nz<L and 0<=nx<R and 0<=ny<C and not visited[nz][nx][ny]:
                if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E':
                    visited[nz][nx][ny] = visited[z][x][y] + 1 
                    q.append((nz,nx,ny))
    
while True:
    L,R,C = map(int, input().split())
    
    if L == 0 and R == 0 and C == 0:
        break 
    
    graph = [[[] * C for _ in range(R)] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)] 
    
    for i in range(L):
        for j in range(R):
            graph[i].append(list(map(str,input().rstrip())))
    

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    sz,sx,sy = i,j,k
                elif graph[i][j][k] == 'E':
                    ez,ex,ey = i,j,k 
    
    bfs() 
    if visited[ez][ex][ey] == 0:
        print("Trapped!")
    else:
        print("Escaped in %d minutes(s)" %graph[ez][ex][ey])
       

    
    
    
