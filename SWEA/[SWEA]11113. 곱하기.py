T = int(input())
for t in range(1,T+1):
    n,a,b = map(int,input().split())
    arr = list(map(int,input().split()))

    cnt = 0
    while cnt < b:
        min_num = min(arr)
        idx = arr.index(min_num)
        arr[idx] = min_num * a
        cnt +=1


    arr.sort()
    for i in range(n):
        arr[i]=arr[i]%(10**9+7)


    print(f'#{t}',end= ' ')
    for i in arr:
        print(i,end=' ')
    print()