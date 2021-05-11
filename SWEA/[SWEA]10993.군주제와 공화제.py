T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        x,y,s = map(int,input().split())
        arr.append([x,y,s])
    result = [0]*n

    rel = [i for i in range(1,n+1)]

    cnt = 0
    while cnt < n:
        x,y,s = arr[cnt]
        check = 0
        for idx,i in enumerate(arr):
            if cnt == idx:
                continue
            else:
                x2,y2,s2 = arr[idx]
                num = s2 / ((x-x2)**2+(y-y2)**2)
                if not check and num > s:
                    check +=1
                    rel[cnt] = rel[idx]
                elif num > s:
                    result[cnt] = 'D'
                    rel[cnt] = -1
                    check += 1
                    break
        cnt += 1
        if not check:
            result[cnt] = 'K'
        elif check == 1:
            pass
    print(rel,result)