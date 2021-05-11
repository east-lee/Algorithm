def main(i,j,m,result,path):
    global max_result
    if m==3:
        if result > max_result:
            max_result = result
        return

    for k in range(4):
        new_path = path[:]
        next_y, next_x = i+direction[k][0], j+direction[k][1]
        if 0<=next_y<N and 0<=next_x<M and [next_y,next_x] not in path:
            new_path.append([next_y,next_x])
            main(next_y,next_x,m+1,result+arr[next_y][next_x],new_path)

def main2(i,j,result):
    global max_result

    check = [
        [[1,0],[2,0],[1,1]],
        [[0,1],[0,2],[1,1]],
        [[1,0],[2,0],[1,-1]],
        [[1,0],[1,-1],[1,1]]
    ]

    for k in range(4):
        now_result = result
        for m in range(3):
            y,x = i+check[k][m][0], j+check[k][m][1]
            if 0<=y<N and 0<=x<M:
                now_result += arr[y][x]
            else:
                now_result = 0
                continue
        if now_result and max_result < now_result: max_result = now_result


if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(N))
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    max_result = 0
    for i in range(N):
        for j in range(M):
            main(i,j,0,arr[i][j],[[i,j]])
            main2(i,j,arr[i][j])

    print(max_result)