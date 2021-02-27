def solution(N, bus_stop):
    answer = list([N ** 2] * N for _ in range(N))
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # bus_stop 초기화
    for i in bus_stop:
        y, x = i
        answer[y - 1][x - 1] = 0

    # bus_stop에서 출발?
    for i in bus_stop:
        y, x = i
        y -= 1
        x -= 1
        visit = list([0] * N for _ in range(N))
        q = []
        q.append([y, x, 0, visit])
        while q:
            print(q)
            start_y, start_x, time, v = q.pop(0)
            for k in range(4):
                next_y, next_x, now_time = start_y + direction[k][0], start_x + direction[k][1], time + 1
                if 0 <= next_y < N and 0 <= next_x < N and not v[next_y][next_x]:
                    if answer[next_y][next_x] < time or answer[next_y][next_x]==0:
                        continue
                    else:
                        v[next_y][next_x] = 1
                        answer[next_y][next_x] = time
                        q.append([next_y, next_x, time, v])
                        v[next_y][next_x] = 0

    return answer
N = 3
bus_stop = [[1,2]]
print(solution(N,bus_stop))