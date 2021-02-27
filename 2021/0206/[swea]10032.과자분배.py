T = int(input())
for t in range(1,T+1):
    n,k = map(int,input().split())
    check = [0]*k

    cnt = 0
    l = 0
    while cnt < n:
        if l >= k:
            l = 0
        check[l] +=1
        cnt += 1
        l+=1
    print(f'#{t} {max(check)-min(check)}')