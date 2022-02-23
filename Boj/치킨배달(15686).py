from itertools import combinations

n,m = map(int, input().split())

graoh = list(list(map(int, input().split())) for _ in range(n))

def chicken_distance(x,y, i,j):
    return abs(x-i) + abs(y-j)
    
house = [] 
chicken = [] 
result = 999999

for i in range(n):
    for j in range(n):
        if graoh[i][j] == 1: house.append((i, j))
        elif graoh[i][j] == 2: chicken.append((i, j))



for ch in combinations(chicken, m):
    distance = 0 

    for h in house:
        each_distance = 999 
        for j in range(m):
            each_distance = min(each_distance, chicken_distance(h[0], h[1], ch[j][0], ch[j][1]))
        
        distance += each_distance
    
    result = min(result, distance)

print(result)
