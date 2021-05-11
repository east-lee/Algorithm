T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list([0]*(N+1) for _ in range(N+1))

    for _ in range(N-1):
        s,e = map(int,input().split())
        arr[s][e] = 1
        arr[e][s] = 1
    
