import sys 

n = list(input())
n.sort(reverse=True)
result = 0 

for i in n:
    result += int(i)
    print(result)

if result % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))