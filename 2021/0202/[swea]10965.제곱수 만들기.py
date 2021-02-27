T = int(input())
for t in range(1,T+1):
    n = int(input())
    check = [0]*10**7
    result = 1
    loop =True
    while loop:
        if n <= 3:
            if check[n]:
                result =  result//n
            else:
                result = result * n
            break
        root_n = int(n**0.5)
        for i in range(2, root_n+1):
            if n%i == 0:
                if check[i] == 0:
                    result *= i
                    check[i] = 1
                else:
                    result = result//i
                    check[i] = 0
                n = n//i
                break
            if i == root_n:
                result *= n
                loop=False
                break
    print(f'#{t} {result}')

