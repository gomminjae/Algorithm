
import sys 
input = sys.stdin.readline
from collections import deque 

a,b,n,m = map(int, input().split())

def bfs():
    while q:
        x = q.popleft() 
        
        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if 0<=nx<=100000 and not visited[nx]:
                    q.append(nx)
                    visited[nx] = 1 
                    graph[nx] = graph[x] + 1
            else:
                nx = x * d[i]
                if 0 <= nx <= 100000 and not visited[nx]:
                    q.append(nx)
                    visited[nx] = 1 
                    graph[nx] = graph[x] + 1 


graph = [0] * 100001
visited = [0] * 100001 
visited[n] = 1 

d = [1,-1,a,-a,b,-b,a,b]
q = deque()
q.append(n)
bfs() 

print(graph[m])