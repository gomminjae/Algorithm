import re
import sys
from turtle import circle 
input = sys.stdin.readline
from collections import deque 

def bfs(a):
    q = deque() 
    q.append(a)
    visited[a] = 1 

    while q:
        node = q.popleft()

        for index,item in enumerate(graph[node]):
            if item and visited[index] == 0:
                visited[index] = 1
                q.append(index)


n = int(input())
m = int(input())
graph = [] 
for _ in range(n):
    graph.append(list(map(int,input().split())))

cities = list(map(int,input().split()))
visited = [0] * n
bfs(cities[0]-1)
result = True 

for city in cities:
    if visited[city-1] == 0:
        result = False 


if result:
    print("YES")
else:
    print("NO")
