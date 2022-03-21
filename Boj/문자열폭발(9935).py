from re import I
import sys 
from collections import deque 
input = sys.stdin.readline
 
S = list(input().rstrip())
bomb = list(input().rstrip())
 
stack = []
 
for i in range(len(S)):
    stack.append(S[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()
 
if stack:
    print("".join(stack))
else:
    print("FRULA")