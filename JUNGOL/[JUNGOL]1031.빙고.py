def check():
    direction = [[0,1],[1,0],[1,1],[1,-1]]
    bingo_num = 0
    for i in range(5):
        for j in range(5):
            if (i==0 or j==0) and board[i][j] == 0:
                for k in range(4):
                    checking = 1
                    y,x = i+direction[k][0],j+direction[k][1]
                    q = []
                    q.append([y,x])
                    while q:
                        y, x = q.pop()
                        if 0<=y<5 and 0<=x<5 and board[y][x] == 0:
                            checking+=1
                            next_y, next_x = y + direction[k][0], x + direction[k][1]
                            q.append([next_y,next_x])
                    if checking==5:
                        bingo_num +=1
    if bingo_num >= 3:
        return True
    else:
        return False

for _ in range(10):
    board = list(list(map(int,input().split())) for _ in range(5))
    ans = list(list(map(int,input().split())) for _ in range(5))
    result = 0
    rr = False
    for i in range(5):
        for j in range(5):
            result += 1
            for m in range(5):
                for n in range(5):
                    if board[m][n] == ans[i][j]:
                        board[m][n] = 0
            rr = check()
            if rr:
                print(result)
                break
        if rr:
            break
