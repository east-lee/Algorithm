for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    while cnt < n-1:
        cnt += 1
        for i in range(n-cnt):
            j = i+1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j],arr[i]
        for i in arr:
            print(i,end=' ')
        print()
