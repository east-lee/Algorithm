def solution(board):
    answer = 0
    n = len(board)-1
    start = [[0,0],[0,1],0,board]
    q = []
    q.append(start)
    while q:

        # 오른쪽, 왼쪽, 위, 아래, 회전(4가지)
        moving = [[0,1],[0,-1],[-1,0],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        location_a, location_b, time,new_board = q.pop(0)

        if location_a[0] == location_b[0] and location_a[1] >location_b[1]: location_a,location_b = location_b,location_a
        elif location_a[1]==location_b[1] and location_a[0] > location_b[0]:location_a,location_b = location_b,location_a

        for k in range(8):
            next_a = [0,0]
            next_b = [0,0]
            using_board = new_board[:]
            if k<=3:
                next_a[0] = location_a[0]+moving[k][0]
                next_a[1] = location_a[1] + moving[k][1]
                next_b[0] = location_b[0]+moving[k][0]
                next_b[1] = location_b[1] + moving[k][1]
            else:
                check = check_rotation(board,moving,k,location_a,location_b,n)
                if check[0]:
                    if k<=5:
                        next_b = location_b
                        next_a[0] = check[1]
                        next_a[1] = check[2]
                    else:
                        next_a = location_a
                        next_b[0] = check[1]
                        next_b[1] = check[2]
            if 0<=next_a[0]<=n and 0<=next_a[1]<=n and 0<=next_b[0]<=n and 0<=next_b[1]<=n and (not using_board[next_a[0]][next_a[1]] or not using_board[next_b[0]][next_b[1]]):
                using_board[next_a[0]][next_a[1]] = 1
                using_board[next_b[0]][next_b[1]] = 1
                q.append([next_a,next_b,time+1,using_board])
            if next_a ==[n,n] or next_b ==[n,n]:
                answer = time
                break

    return answer

def check_rotation(board,moving,k,i,j,n):
    if k == 4 or k==5: # 위에있는게 오른쪽아래로 내려오는경우
        y,x=i[0],i[1]
    else:
        y,x = j[0],j[1]
    y += moving[k][0]
    x += moving[k][1]
    if 0<=x<=n and 0<=y<=n and board[y][x]:
        return [False]
    else:
        return [True,y,x]




board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
