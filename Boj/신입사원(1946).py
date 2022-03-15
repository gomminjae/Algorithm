import sys 
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    newbee = []
    count = 1
    n = int(input())
    for i in range(n):
        resume, interview = map(int, input().split())
        newbee.append([resume,interview])
    
    
    newbee.sort() 
    first = newbee[0][1]

    for i in range(1,n):
        if first > newbee[i][1]:
            count += 1 
            first = newbee[i][1]

    print(count)
