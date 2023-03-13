import sys
input = sys.stdin.readline
from collections import deque 

def bfs(k,v):
    q = deque()
    q.append((v,10e9))
    visited[v] = 1 
    count = 0 
    
    while q:
        node,r = q.popleft()
        
        for nv,nr in graph[node]:
            nr = min(r,nr)

            if nr >= k and not visited[nv]:
                q.append((nv,nr))
                visited[nv] = 1 
                count += 1 
    return count 
    
N,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p,q,r = map(int, input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))

for _ in range(Q):
    k,v = map(int, input().split())
    visited = [0] * (N+1)
    print(bfs(k,v))

    
