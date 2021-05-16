def main():
    visited = list([0]*M for _ in range(N))
    result_arr = list([0]*M for _ in range(N))
    result_arr[0][0] = 1

    for i in range(N):
        for j in range(M):
            if i+j == 0 or visited[i][j]: continue
            result_arr, visited = dfs(i,j,result_arr,visited)

    # for i in result_arr:
    #     print(i)
    print(result_arr[N-1][M-1])


def dfs(i,j,result_arr,visited):
        for k in range(4):
            y,x = i+direction[k][0], j+direction[k][1]
            if 0<=y<N and 0<=x<M and arr[y][x] > arr[i][j]:
                if visited[y][x] ==0:
                    result_arr,visited = dfs(y,x,result_arr,visited)
                    result_arr[i][j] += result_arr[y][x]
                else:
                    result_arr[i][j] += result_arr[y][x]
        visited[i][j] = 1
        return [result_arr,visited]



direction = [[-1,0],[1,0],[0,-1],[0,1]]


if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(N))
    main()