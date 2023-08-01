n = int(input())
count = 0

for i in range(1, n+1):
    result = set()
    for j in range(1, i+1):
        if i%j==0:
            result.add(j)
    result = list(result)
    count += sum(result)

print(count)