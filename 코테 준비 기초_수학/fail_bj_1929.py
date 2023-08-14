'''
inp = list(map(int, input().split()))
result = []

# 리스트 생성
for i in range(inp[0], inp[1]+1):
    result.append(i)

# 특정 수의 배수에 해당하는 수를 모두 지우기
for i in range(2, inp[1]+1):
    if(i == 0): continue
    for j in range (i*2, inp[1]+1, i):
        if j in result:
            result[result.index(j)] = 0

for i in result:
    if i != 0:
        print(i)
'''

inp = list(map(int, input().split()))
a = [False,False] + [True]*(inp[1]-1)
primes=[]

for i in range(inp[0],inp[1]+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, inp[1]+1, i):
        a[j] = False


for i in a:
    if i != 0:
        print(i)