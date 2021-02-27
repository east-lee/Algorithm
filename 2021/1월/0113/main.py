def solution(N, bus_stop):
    answer = list([-1] * N for _ in range(N))
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in bus_stop:
        y, x = i
        answer[y-1][x-1] = 0
    for i in range(N):
        for j in range(N):
            if answer[i][j]:
                visit = list([0] * N for _ in range(N))
                start_y, start_x = i, j
                q = []
                q.append([start_y, start_x, 0])
                while q:
                    y, x, time = q.pop(0)
                    for k in range(4):
                        next_y, next_x = y + direction[k][0], x + direction[k][1]
                        if 0 <= next_y < N and 0 <= next_x < N and not visit[next_y][next_x]:
                            if answer[next_y][next_x] == 0:
                                answer[i][j] = time + 1
                                q = []
                                break
                            else:

                                visit[next_y][next_x] = 1
                                q.append([next_y, next_x, time + 1])

    return answer

N = 3
bus_stop = [[1,2]]
print(solution(N,bus_stop))