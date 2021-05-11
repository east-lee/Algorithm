def dfs(n,m,k,who,cc):
    global result

    if who == 0: n-=1
    elif who == 1:m-=1
    else:k-=1
    if n==-1 or m==-1 or k==-1:
        if n==-1:
            result += 1
        return
    dfs(n,m,k,0,1)
    dfs(n, m, k, 1,1)
    dfs(n, m, k, 2,1)


T = int(input())
for t in range(1,T+1):
    N,M,K = map(int,input().split())
    result = 0
    dfs(N,M,K,0,0)
    print(f'#{t} {result}')