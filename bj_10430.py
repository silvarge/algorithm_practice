# 함수 정의
def mod(a,b,c):
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)

# 값 입력
a, b, c = map(int, input().split())

mod(a,b,c)
