T= int(input())
for t in range(1,T+1):
    n = int(input())
    arr = list(list(input()) for _ in range(n))

    direction = [[0,1],[1,1],[1,-1],[1,0]]

    result = 'NO'
    breaker = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] =='o':
                
                for k in range(4):
                    cnt = 1
                    y,x=i+direction[k][0],j+direction[k][1]
                    loop = True
                    while loop:
                        if 0<=x<n and 0<=y<n and arr[y][x] == 'o':
                            
                            cnt += 1
                            y,x=y+direction[k][0],x+direction[k][1]
                        else:
                            if cnt >= 5:
                                result = 'YES'
                                breaker = True
                                break
                            else:
                                break
            if breaker: break
        if breaker:break
    print(f'#{t} {result}')
                        
