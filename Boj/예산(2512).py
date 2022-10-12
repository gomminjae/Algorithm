import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort() 

start = 0
end = max(arr)

while start <= end:
    total = 0
    mid = (start+end)//2 
    
    for x in arr:
       if x >= mid:
           total += mid 
       else:
           total += x 
    if total <= m:
        start = mid + 1 
    else:
        end = mid - 1 
        
print(end)