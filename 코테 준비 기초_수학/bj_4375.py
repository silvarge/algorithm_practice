while True:
    # 입력
    try:
        n = int(input())
    except:
        break

    i = 1
    num = 0

    while True:
        num = (num * 10) + 1
        m = num % n
        if(m==0):
            print(i)
            break
        i+=1
