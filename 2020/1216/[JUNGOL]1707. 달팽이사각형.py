for _ in range(10):
    n = int(input())
    result = list([0]*n for _ in range(n))
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    d = 0
    cnt = 1
    result[0][0] = 1
    y, x = 0,0
    while cnt < n**2:
        cnt += 1
        i = y + direction[d][0]
        j = x + direction[d][1]
        if 0<=i<n and 0<=j<n and not result[i][j]:
            y,x = i,j
            result[i][j] = cnt
        else:
            d = (d+1)%4
            y,x = y+direction[d][0], x+direction[d][1]
            result[y][x] = cnt
    for i in range(n):
        for j in range(n):
            print(result[i][j],end = ' ')
        print()

