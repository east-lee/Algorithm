for _ in range(10):
    n,m = map(int,input().split())
    result  = [[0]*n for _ in range(n)]
    result[0][0] = 1
    for i in range(1,n):
        for j in range(n):
            if j ==0:
                result[i][j]=result[i-1][j]
            else:
                result[i][j]= result[i-1][j] + result[i-1][j-1]
    if m == 2:
        result = result[::-1]
    if m==3:
        result = result[::-1]
        N = len(result)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[N - 1 - c][r] = result[r][c]
        result= ret


    for i in range(n):
        if i >0 and m==2:
            print(' '*i,end=' ')
        for j in range(n):
            if result[i][j]:
                print(result[i][j],end = ' ')
            else:
                print(' ', end = ' ')
        print()

