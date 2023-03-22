
import sys 
input = sys.stdin.readline
from collections import deque 

def bfs():
    q = deque()
    q.append((s,""))

    if s == t:
        return 0 

    while q:
        num,cal = q.popleft()

        if num == t:
            return cal
        
        tmp = num ** 2
        if 0<=tmp<=MAX and tmp not in visited:
            visited.add(tmp)
            q.append((tmp,cal+'*'))
        
        tmp = num + num
        if 0<=tmp<=MAX and tmp not in visited:
            visited.add(tmp)
            q.append((tmp,cal+'+'))
        tmp = num-num
        if 0<=tmp<=MAX and tmp not in visited:
            visited.add(tmp)
            q.append((tmp,cal+'-'))
        if num != 0:
            tmp = 1
            if 0<=tmp<=MAX and tmp not in visited:
               visited.add(tmp)
               q.append((tmp,cal+'/'))
    return -1 

s,t = map(int, input().split())

result = ""

q = deque() 
q.append((s,""))
MAX = 10e9 
visited = set([s])

result = bfs()
print(result)

