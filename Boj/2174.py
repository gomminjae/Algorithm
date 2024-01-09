import sys 
input = sys.stdin.readline

a,b = map(int, input().split())
n,m = map(int, input().split())

graph = [[0]*m for _ in range(n)]
robots = []
for i in range(n):
    x,y,d = map(str,input().split())
    
    direction_x = int(x) - 1 
    direction_y = int(y) - 1 
    
    graph[direction_x][direction_y] = i
    robots.append((direction_x,direction_y,d))

for i in range(m):
    a,direction,c = map(str,input().split())
    robot_num = int(a) - 1 
    iterator = int(c)
    
    if direction == 'F':
        x = robots[robot_num][0]
        y = robots[robot_num][1]
        
        if robots[robot_num][2] == 'N':
            y += 1 
            robots[robot_num][1] = chr(y)
            if x < 0 or x > n or y < 0 or y > m:
                print(f"Robot {graph[x][y-1]} crashes into the wall")
                break
            
            elif graph[x][y] != 0:
                print(f"Robot {graph[x][y-1]} crashes into {graph[x][y]}")
                break
                
            
        
    
    