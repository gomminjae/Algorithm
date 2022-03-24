from os import popen
import sys 
input = sys.stdin.readline

from collections import deque 
import copy

n,m = map(int, input().split())
graph = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    #global graph
    copy_graph = copy.deepcopy(graph)
    queue = deque()

    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                queue.append((nx,ny))
    global answer 
    count = 0 

    for i in range(n):
        count += copy_graph[i].count(0)

    answer = max(answer,count)


def wall(count):
    if count == 3:
        bfs() 
        return 
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0 
answer = 0 

for _ in range(m):
    graph.append(list(map(int, input().split())))

wall(0)
print(answer)