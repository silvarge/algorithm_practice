import math, sys

max = 1000000
# max = 100
array = [True for i in range(max+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화
hasGold = False
input = sys.stdin.readline

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(max))+1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i*j <= max:
            array[i*j] = False
            j += 1


while True:

    hasGold = False
    inp = int(input().rstrip())

    if inp < 6 or inp > max or inp == 0:
        break

    for i in range(3, max+1, 2):
        if array[i] and array[inp - i]:
            hasGold = True
            print(inp, "=", i, "+", inp-i)
            break
        
    if not hasGold:
        print("Goldbach's conjecture is wrong.")
        break