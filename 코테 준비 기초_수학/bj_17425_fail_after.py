count = int(input())
sum = []

for c in range(count):
    try:
        n = int(input())
    except:
        break

    sum_n = 0

    # 약수 합 계산
    for i in range(1, n+1):
        sum_n += (n//i)*i
    sum.append(sum_n)

for num in sum:
    print(num)
