for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    cnt = 1
    while cnt < n:
        check = cnt
        for i in range(cnt,0,-1):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                result += 1
        cnt +=1
    print(result)

