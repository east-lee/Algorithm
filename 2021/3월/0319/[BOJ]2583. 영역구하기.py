direction = [[-1,0],[1,0],[0,-1],[0,1]]

if __name__ == "__main__":
    M,N,K = map(int,input().split())
    check = list([0]*N for _ in range(M))
    for _ in range(K):
        x1, y1, x2, y2 = map(int,input().split())
        for i in range(y1,y2):
            for j in range(x1,x2):
                check[i][j] = 1
    result = []
    for i in range(M):
        for j in range(N):
            cnt = 0
            if check[i][j] == 0:
                check[i][j] = 1
                q = [[i,j]]
                cnt += 1
                while q:
                    y,x = q.pop()
                    for k in range(4):
                        next_y,next_x = y+direction[k][0],x+direction[k][1]
                        if 0<=next_y<M and 0<=next_x<N and check[next_y][next_x] == 0:
                            cnt += 1
                            check[next_y][next_x] = 1
                            q.append([next_y,next_x])
                result.append(cnt)

    result.sort()
    print(len(result))
    for i in result: print(i,end=' ')

    print()

