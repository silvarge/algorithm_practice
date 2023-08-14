import sys, copy

input = sys.stdin.readline
candy = list()
max_eat = [0] * 4 # [C, P, Z, Y] 최대로 먹을 수 있는 사탕 개수 세기 
eat = 0

# 입력
n = int(input().strip())

for i in range(n):
    temp = list(input().strip())
    candy.append(temp)

def count_row (n, candy, eat):
    for i in range(n):
        max_eat = [0] * 4
        for j in range(n):
            if candy[i][j]=="C":
                max_eat[0] += 1
            elif candy[i][j]=="P":
                max_eat[1] += 1
            elif candy[i][j]=="Z":
                max_eat[2] += 1
            else: max_eat[3] += 1
        if(eat == n): break
        eat = max(max_eat) if eat < max(max_eat) else eat
    return eat

def count_column (n, candy, eat):
    for i in range(n):
        max_eat = [0] * 4
        for j in range(n):
            if candy[j][i]=="C":
                max_eat[0] += 1
            elif candy[j][i]=="P":
                max_eat[1] += 1
            elif candy[j][i]=="Z":
                max_eat[2] += 1
            else: max_eat[3] += 1
        if(eat == n): break
        eat = max(max_eat) if eat < max(max_eat) else eat
    return eat

# ! 만약 n이 되면 그냥 그대로 끝
# 바꾸기 전 최대로 먹을 수 있는 사탕 개수
# 가로 개수
# for i in range((n-1)*(n-1)):
#     print(i//(n-1), i%(n-1), candy[i//(n-1)][i%(n-1)])

eat = max(eat, count_row(n, candy, eat), count_column(n, candy, eat))

# 가로 변경 -> 세로 사탕 개수 재확인
print("가로 변경 =======")
for i in range(n-1):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        eat = max(eat, count_column(n, candy, eat))
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if eat == n: break

print("세로 변경 =======")
# 세로 변경 -> 가로 사탕 개수 재확인
for i in range(n-1):
    for j in range(n-1):
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        eat = max(eat, count_row(n, candy, eat))
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

        if eat == n: break

print(eat)