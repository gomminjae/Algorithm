T = int(input())

def dfs(x, y):

    

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False 

    if graph[x][y] == 1:
        graph[x][y] = 0
    
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True 
    return False 

loop = 0 

for _ in range(T):

    count = 0 
    
    n,m,k = map(int, input().split())
 
    graph = [[0] * n for _ in range(m)]


    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1 

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]


    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                count += 1 

    print(count )
    


    
    






