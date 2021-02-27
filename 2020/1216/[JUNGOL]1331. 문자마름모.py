for _ in range(10):
    n = int(input())
    n = 2*n -1
    result = list([0]*n for _ in range(n))
    direction = [[1,-1],[1,1],[-1,1],[-1,-1]]
    y, x= 0, n//2
    # print(chr(65),chr(90))
    chr_num = 65
    q= []
    q.append([y,x])
    d = 0
    cnt = (n+1) //2
    c = 0
    while q:
        i,j = q.pop()
        result[i][j] = chr(chr_num)
        c+=1
        y = i + direction[d][0]
        x = j + direction[d][1]
        if 0<=x<n and 0<=y<n and not result[y][x] and c<cnt and d==0:
            result[y][x] = chr(chr_num)
            q.append([y,x])
        elif 0 <= x < n and 0 <= y < n and not result[y][x] and c < cnt-1 and d != 0:
            result[y][x] = chr(chr_num)
            q.append([y, x])
        else:
            d = (d+1)%4
            c = 0
            if d == 0:
                q.append([i,j-1])
                cnt -= 1
            else:
                y = i + direction[d][0]
                x = j + direction[d][1]
                if not result[y][x]:
                    q.append([y,x])
                    result[y][x] = chr(chr_num)



        chr_num += 1
        if chr_num > 90:
            chr_num = 65

    result[n//2][n//2] = chr(chr_num)
    for i in range(n):
        for j in range(n):
            if result[i][j]:
                print(result[i][j], end = ' ')
            else:
                print(' ',end= ' ')
        print()
