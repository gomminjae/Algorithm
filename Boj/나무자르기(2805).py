import sys 
input = sys.stdin.readline

n,m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort() 

start = 0
end = max(trees)

while start <= end:
    total = 0 
    mid = (start+end) // 2
    
    for x in trees:
        if x > mid:
            total += x - mid 
    
    if total < m:
        end = mid - 1 
    else:
        result = mid
        start = mid + 1 
        
print(result)
         
    