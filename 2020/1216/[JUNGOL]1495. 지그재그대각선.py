for _ in range(10):
    n = int(input())
    result = list([0]*n for _ in range(n))
    cnt = 0
    direction = [[1,-1],[-1,1]]
    d = 0
    y, x = 0, 0
    while cnt < n**2-1:
        if y>=n or x>n:
            break
        cnt += 1
        result[y][x] = cnt
        if not d:
            i = y + direction[d][0]
            j = x + direction[d][1]
            if 0<=i<n and 0<=j<n:
                y, x= i, j
            elif 0<=y+1<n:
                y, x = y+1, x
                d = 1
            else:
                d= 1
                y,x = y, x+1

        else:
            i = y + direction[d][0]
            j = x + direction[d][1]
            if 0<=i<n and 0<=j<n:
                y,x, = i,j
            elif 0<=x+1<n:
                y, x = y, x + 1
                d = 0
            else:
                y,x=y+1,x
                d = 0
    result[n-1][n-1] = n**2
    for i in range(n):
        for j in range(n):
            print(result[i][j], end = ' ')
        print()