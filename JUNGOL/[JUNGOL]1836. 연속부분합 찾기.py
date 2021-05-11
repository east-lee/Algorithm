for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    max_result = sum(arr)
    for i in range(n):
        for j in range(i,n+1):
            if max_result < sum(arr[i:j]):
                max_result = sum(arr[i:j])
    print(max_result)