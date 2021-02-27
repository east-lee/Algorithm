T = int(input())
for t in range(1,T+1):
    arr = input()
    check = {}
    for i in arr:
        if i in check:
            if check[i] == 1:
                check[i] = 0
            else:
                check[i] = 1
        else:
            check[i] = 1
    result = ''
    check = sorted(check.items())
    for a,b in check:
        if b!=0:
            result += a
    if not result: result = 'Good'
    print(f'#{t} {result}')
