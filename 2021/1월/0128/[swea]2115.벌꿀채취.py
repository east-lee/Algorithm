T = int(input())
for t in range(1,T+1):
    n,m,c = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(n))
    ## 문제 이해가잘..?