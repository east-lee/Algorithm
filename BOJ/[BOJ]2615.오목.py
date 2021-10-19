def get_data():
    N = 19
    game_baord = list(list(map(int,input().split())) for _ in range(N))

    return [N, game_baord]

def checking(i,j,stone_color):

    for k in range(4):
        cnt = 0
        save_list = []
        y, x = i ,j

        while 0<=y<N and 0<=x<N and game_board[y][x] == stone_color:
            cnt += 1
            save_list.append([y, x])

            y += direction[k][0]
            x += direction[k][1]

        if cnt == 5:
            if 0<=i-direction[k][0]<N and 0<=j-direction[k][1] <N and game_board[i-direction[k][0]][j-direction[k][1]] == stone_color:
                continue
            else:
                return save_list
    return False


if __name__ == "__main__":
    N, game_board = get_data()
    direction = [[-1,1], [0,1], [1,1], [1,0]]
    result = False

    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                continue
            else:
                result = checking(i,j,game_board[i][j])
                if not result:
                    continue
                else:
                    break
        if result: break

    if not result:
        print(0)
    else:
        result.sort(key=lambda x:(x[1], x[0]))
        result_y, result_x = result[0][0], result[0][1]
        # print(result)
        print(game_board[result_y][result_x])
        print(result_y + 1, end= " ")
        print(result_x + 1)





