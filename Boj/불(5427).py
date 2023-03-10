import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()

        if x == 0 or y == 0 or x == (m-1) or y == (n-1):
            return visited[x][y]
        spread()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and visited[nx][ny] == 0:
                if graph[nx][ny] == '.':
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return 0


def spread():
    for i in range(len(fire)):
        x,y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == '.':
                    fire.append((nx,ny))


for _ in range(T):
    graph = []
    m,n = map(int,input().split())
    visited = [[0]*m for _ in range(n)]

    fire = deque()

    for i in range(n):
        for j in range(m):
            graph.append(list(map(str,input().rstrip())))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                x,y = i,j

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                fire.append((i,j))
    result = bfs(x,y)

    if result == 0:
        print("IMPOSSIBLE")
    else:
        print(result)






