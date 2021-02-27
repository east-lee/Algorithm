for _ in range(10):
    n = int(input())
    result = list([-1]*n for _ in range(n))
    start_y, start_x = 0,0
    direction = [[1,1],[0,-1],[-1,0]]

    d = 0
    cnt = 0
    q = []
    q.append([start_y,start_x])
    while q:
        i,j = q.pop()
        if result[i][j]!=-1:
            break
        if cnt >9:
            cnt = 0
        result[i][j] = cnt

        if i+direction[d][0]<0 or i+direction[d][0]>=n or j+direction[d][1]<0 or j+direction[d][1]>=n or result[i+direction[d][0]][j+direction[d][1]]!=-1:
            d = (d+1)%3
            q.append([i + direction[d][0], j + direction[d][1]])
        else:
            q.append([i+direction[d][0],j+direction[d][1]])
        cnt += 1

    for i in range(n):
        for j in range(n):
            if result[i][j] != -1:
                print(result[i][j],end=' ')
            else:
                print(' ',end=' ')
        print()

