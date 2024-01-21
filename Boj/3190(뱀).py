import sys 
from collections import deque
input = sys.stdin.readline
    
#대가리 방향 전환 
def change(direction):
    global snake_direction

    if direction == 'L':
        if snake_direction == 'L':
            snake_direction = 'D'
        elif snake_direction == 'R':
            snake_direction = 'U'
        elif snake_direction == 'U':
            snake_direction = 'L'
        else:
            snake_direction = 'R'
    else:
        if snake_direction == 'L':
            snake_direction = 'U'
        elif snake_direction == 'U':
            snake_direction = 'R'
        elif snake_direction == 'D':
            snake_direction = 'L'
        else:
            snake_direction = 'D'
#이동
def move(x,y):
    global snake 
    global snake_direction

    
    if snake_direction == 'R':
        if check(x,y+1):
            snake.append([x,y+1])
        else:
            snake.append([x,y+1])
            snake.pop(0)

    elif snake_direction == 'U':
        if check(x-1,y):
            snake.append([x-1,y])
        else:
            snake.append([x-1,y])
            snake.pop(0)
    elif snake_direction == 'D':
        if check(x+1,y):
            snake.append([x+1,y])
        else:
            snake.append([x+1,y])
            snake.pop(0)
    else:
        if check(x,y-1):
            snake.append([x,y-1])
        else:
            snake.append([x,y-1])
            snake.pop(0)

#사과체크 
def check(a,b):
    if 0<=a<n and 0<=b<n and graph[a][b] == 1:
        graph[a][b] = 0 
        print(f"열매 발견함{a,b}")
        return True 
    else:
        return False 


n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    row,col = map(int,input().split())
    graph[row-1][col-1] = 1 

l = int(input())
commands = []
for _ in range(l):
    x,c = map(str,input().split())
    commands.append([x,c])

time = 0 
snake = [[0,0]] 
snake_direction = 'R'
x,command = commands.pop(0)

while True:
    #print(f"뱀 머리 방향: {snake_direction}") 
    move(snake[-1][0],snake[-1][1])
    head = snake[-1]
    time += 1 
    print(f"시간====={time}")
    print(x,command)

    if time == int(x):
        #방향 변환됨
        change(command)
        print(f"뱀머리방향===={snake_direction,time}")
        if len(commands) > 0:
            x,command = commands.pop(0)
    

    print(f"머리위치====={head}")
    print(f"뱀 몸통====={snake[:len(snake)-1]}\n")

    if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n:
        print("벽에 부딪힘")
        print(time)
        break

    if head in snake[:len(snake)-1]:
        print("몸통에 부딪힘")
        print(time)
        break


        






    
    



