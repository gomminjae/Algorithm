import sys 
from collections import deque 
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque() 
queue.append(1)

def bfs():
    while queue:
        now = queue.popleft() 
        for i in graph[now]:
            if result[i] == 0:
               result[i] = now
               queue.append(i)
bfs() 
answer = result[2:]

for i in answer:
    print(i)