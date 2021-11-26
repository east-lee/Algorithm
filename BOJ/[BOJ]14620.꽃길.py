import sys

def get_data():
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    return [N, arr]

def select_point(selected_point=[] ,cnt=0):

    if cnt == 3:
        solution(selected_point)
        return
    pre_y, pre_x = [0, -1] if not selected_point else selected_point[-1]

    for i in range(pre_y, N-1):
        for j in range(1, N-1):
            if i == pre_y and pre_x >= j:
                continue
            next_selected_point = selected_point[:]
            next_selected_point.append([i,j])
            select_point(next_selected_point, cnt+1)

def solution(selected_point):
    global result, visited
    # print(selected_point)
    point_price = 0
    for y, x in selected_point:
        point_price += arr[y][x]

        if visited[y][x]:
            visited = [[False] * N for _ in range(N)]
            return
        visited[y][x] = True
        for k in range(4):
            ny, nx = y + direction[k][0], x + direction[k][1]

            if 0>ny or ny >= N or 0>nx or nx>=N:
                visited = [[False] * N for _ in range(N)]
                return

            if visited[ny][nx]:
                # print("_-------------------------")
                # for line in visited: print(line)
                # print(selected_point)
                visited = [[False] * N for _ in range(N)]
                return

            visited[ny][nx] = True
            point_price += arr[ny][nx]

    visited = [[False]*N for _ in range(N)]
    # print("result!!!!!!!!!!", point_price)
    result = min(result, point_price)



if __name__ == "__main__":
    N, arr = get_data()
    direction = [[-1,0], [1,0], [0,-1], [0,1]]
    visited = [[False]*N for _ in range(N)]
    result = sys.maxsize

    select_point()

    print(result)