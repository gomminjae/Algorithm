n = int(input())

words = [] 

for _ in range(n):
    words.append(list(map(lambda x: ord(x) - 65, input())))

alphabets = [0] * 26

for word in words:
    for idx, char in enumerate(word[::-1]):
        alphabets[char] += (10 ** idx)

alphabets.sort(reverse=True)
sum_value = 0 
num = 9 

for i in range(9):
    sum_value += num * alphabets[i]
    num -= 1 


print(sum_value)

    
    



    

