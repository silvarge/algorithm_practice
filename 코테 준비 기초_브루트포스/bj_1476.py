import sys

input = sys.stdin.readline
cal = list(map(int, input().split()))
count = [0,0,0]
result = 0

while True:
    result += 1
    count = list(map(lambda x:x +1, count))
    
    if count[0]%16 == 0: count[0] = 1
    if count[1]%29 == 0: count[1] = 1
    if count[2]%20 == 0: count[2] = 1

    if cal == count:
        print(result)
        break