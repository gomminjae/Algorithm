import sys
from textwrap import fill
from turtle import right 
input = sys.stdin.readline



def fill_zero(ip):
    print(ip.zfill(4))
    return ip.zfill(4)


ip = input().rstrip()

left = []
right = []
result = []

if '::' in ip:
    tmp =  ip.split("::")
    left = tmp[0].split(':')
    right = tmp[1].split(':')
else:
    left = ip.split(":")

    

if len(right) == 0:
    for i in range(len(left)):
        result.append(fill_zero(left[i]))

else:
    for i in range(len(left)):
        result.append(fill_zero(left[i]))
    for i in range(8-(len(left)+len(right))):
        result.append('0000')
    for i in range(len(right)):
        result.append(fill_zero(right[i]))
    

print(':'.join(result))