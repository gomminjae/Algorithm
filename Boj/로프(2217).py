import sys
from typing import Reversible 
input = sys.stdin.readline 

n = int(input())

li = [] 
result = []
for _ in range(n):
    li.append(int(input()))

li.sort(reverse=True)

for i in range(n):
    result.append(li[i]*(i+1))

print(max(result))
