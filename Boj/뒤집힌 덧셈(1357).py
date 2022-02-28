

li = list(input().split())


def rev(s):
     return s[::-1]

sum = 0

for i in li:
    a = int(rev(i))
    sum += a 

s_sum = str(sum)


print(int(s_sum[::-1]))