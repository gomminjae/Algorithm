import sys 

input = sys.stdin.readline

while True:
    li = []
    li2 = []
    s = input()
    if s == '.':
        break
    
    for ch in li:
        if ch == "[":
            li.append(1)
        elif ch == "(":
            li2.append(1)
        if len(li) != 0:
            if ch == "]":
                li.pop() 
            elif ch == ")":
                li2.pop()

    if s == '.':
        break
                
        
    if len(li) == 0 and len(li2) == 0:
        print("yes")
    else:
        print("no")

    