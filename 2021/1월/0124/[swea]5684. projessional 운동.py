T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    arr = list([0]*(N+1) for _ in range(N+1))
    result = -1
    for _ in range(M):
        s,e,c=map(int,input().split())
        arr[s][e] = c
    check = [0]*(N+1)

    for i in range(1,N+1):
        num = 0
        start = i
        end = arr[]
        pass

## 해당문제 파이썬 런타임 오류 있음