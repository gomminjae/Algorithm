from sys import stdin
from collections import deque
input = stdin.readline


n,start,end = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

def solv():
    visited = [False]*(n+1)
    q = deque([(start,0,0)])
    visited[start] = True
    while q:
        now,total,max_cost = q.popleft()
        if now == end:
            print(total-max_cost)
            return
        for nxt,cost in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.appendleft((nxt,total+cost,max(max_cost,cost)))
solv()