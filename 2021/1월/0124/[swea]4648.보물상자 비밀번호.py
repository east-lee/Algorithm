T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    arr=input()

    check = []

    mod_num = N//4

    cnt = 0
    while cnt < mod_num:
        for i in range(4):
            s,e=mod_num*i,mod_num*i+mod_num
            check.append(arr[s:e])
        arr = arr[1:] + arr[:1]
        cnt += 1
    check=list(set(check))
    for i in range(len(check)):
        oxstr = check[i]
        oxstr = '0x'+oxstr
        num = int(oxstr,16)
        check[i] = num
    check.sort(reverse=True)
    
    print(f'#{t} {check[K-1]}')
