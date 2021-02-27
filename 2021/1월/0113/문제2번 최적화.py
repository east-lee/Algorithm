def solution(N, bus_stop):
    answer = list([-1] * N for _ in range(N))
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in bus_stop:
        y, x = i
        answer[y - 1][x - 1] = 0
    for i in range(N):
        for j in range(N):
            if answer[i][j] >= 0:
                continue
            else:
                visit = list([0] * N for _ in range(N))
                q = []
                q.append([i, j, 0, [], visit])
                while q:
                    start_y, start_x, time, route, v = q.pop(0)
                    for k in range(4):
                        visit_copy = v[:]
                        next_y, next_x = start_y + direction[k][0], start_x + direction[k][1]
                        if 0 <= next_y < N and 0 <= next_x < N and not visit_copy[next_y][next_x]:
                            if answer[next_y][next_x] == 0:
                                answer[i][j] = time + 1
                                cnt = 0
                                while cnt < len(route):
                                    check_y, check_x = route[cnt]
                                    answer[checl_y][check_x] = time - cnt
                                    cnt += 1
                                q = []
                                break
                            else:
                                visit_copy[next_y][next_x] = 1
                                route.append([next_y, next_x])
                                q.append([next_y, next_x, time + 1, route, visit_copy])
                                route.pop()

    return answer

N = 3
bus_stop = [[1,2]]
print(solution(N,bus_stop))