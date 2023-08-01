# 입력
count = int(input())
divisor = list(map(int, input().split()))

if not(count > 50 or count != len(divisor)) :    
    divisor.sort()
    print(divisor[0]*divisor[-1])
