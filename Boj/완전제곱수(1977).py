
import math
m = int(input())
n = int(input())

result = [] 

for i in range(m,n+1):
    num = int(math.sqrt(i))
    
    if i == num ** 2:
        #print(i)
        result.append(i)

if result == []:
    print(-1)

else:
    print(sum(result))
    print(min(result))





