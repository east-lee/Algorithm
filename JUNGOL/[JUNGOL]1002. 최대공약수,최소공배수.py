for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    result = 0
    for i in range(1,arr[0]+1):
        cnt = 0
        for j in arr:
            if j%i == 0:
                cnt +=1
        if cnt == n:
            result = i
    rr = 0
    for i in range(1,2000000000//arr[0]):
        cnt = 0
        rr = arr[0]*i
        for j in arr:
            if rr%j == 0:
                cnt +=1
        if cnt == n:
            break

    print(f'{result} {rr}')

