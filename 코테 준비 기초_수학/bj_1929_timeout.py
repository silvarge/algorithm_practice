inp = list(map(int, input().split()))
result = []

for i in range(inp[0], inp[1]+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1

    if cnt == 2:
        result.append(i)


for i in result:
    print(i)