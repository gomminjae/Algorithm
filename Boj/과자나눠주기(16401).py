import sys 
input = sys.stdin.readline

m,n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = max(arr)


while start <= end:
    count = 0 
    mid = (start+end) // 2 
    
    for x in arr:
        if x >= mid:
            count += (x // mid)
        else:
            continue
    
    if count >= m:
        result = mid
        start = mid + 1 
    else:
        end = mid - 1 

print(result)
