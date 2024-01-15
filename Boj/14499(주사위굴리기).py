import sys 
input = sys.stdin.readline

#동서북남 
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def move(command,dice,r,c): 
    global x
    global y
    global n
    global m
    nr = r + dr[command - 1]
    nc = c + dc[command - 1]

    #print(f"===={nr,nc}")

    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        return 

    x = nr
    y = nc

    under = dice[0]
    front = dice[1]
    right = dice[2]
    left = dice[3]
    back = dice[4]
    up = dice[5]


    if command == 1:
        # 밑 오 왼 위 
        newValue = graph[nr][nc]

        if newValue == 0:
            graph[nr][nc] = right
            dice[0] = right
            dice[3] = under 
            dice[5] = left 
            dice[2] = up
        
        else:
            graph[nr][nc] = 0 
            dice[0] = newValue
            dice[3] = under 
            dice[5] = left 
            dice[2] = up
    
    elif command == 2:
        newValue = graph[nr][nc]

        if newValue == 0:
            graph[nr][nc] = left 
            dice[0] = left 
            dice[2] = under
            dice[5] = right
            dice[3] = up
        else:
            graph[nr][nc] = 0 
            dice[0] = newValue
            dice[2] = under
            dice[5] = right
            dice[3] = up
    elif command == 3:
        newValue = graph[nr][nc]


        # 밑앞오왼뒤위
        if newValue == 0:
            graph[nr][nc] = front 
            dice[0] = front
            dice[1] = up 
            dice[4] = under 
            dice[5] = back 
            
        else:
            graph[nr][nc] = 0 
            dice[0] = newValue
            dice[1] = up 
            dice[4] = under 
            dice[5] = back 
    else:
        newValue = graph[nr][nc]
        if newValue == 0:
            graph[nr][nc] = back 
            dice[0] = back 
            dice[1] = under 
            dice[5] = front
            dice[4] = up 


        else:
            graph[nr][nc] = 0 
            dice[0] = newValue
            dice[1] = under 
            dice[5] = front
            dice[4] = up 
    #print(f"========>dice{dice}")
    print(dice[5])

n,m,x,y,k = map(int, input().split())
graph = []

# 밑앞오왼뒤위
dice = [0,0,0,0,0,0]
for _ in range(n):
    graph.append(list(map(int,input().split())))
#초기 밑면 셋팅 
dice[0] = graph[x][y]
graph[x][y] = 0 
commands = list(map(int,input().split()))

for command in commands:
    move(command,dice,x,y)     

        
        


        
        


        


