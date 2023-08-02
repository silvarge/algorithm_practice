n = list(map(int, input().split()))
n.sort(reverse=True)

b = n[0]
gcd = n[1]
lcm = 1

# 최대공약수
while True:
    if (b%gcd != 0):
        temp = b%gcd
        b = gcd
        gcd = temp
    else:
        break

# 최소공배수
lcm = (n[0] * n[1])//gcd

print(gcd)
print(lcm)