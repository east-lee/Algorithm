from collections import deque

def solution():

    dq = deque()
    dq.append([start_point, 0])
    visited = [False] * N
    visited[start_point] = True

    while dq:
        my_point, cnt = dq.popleft()
        # print(my_point, maze[my_point])
        if my_point == end_point:
            return cnt
        for i in range(maze[my_point]+1):
            if i == 0: continue
            next_point = i + my_point
            if next_point >= N or visited[next_point]:
                continue
            visited[next_point] = True
            dq.append([next_point, cnt+1])

    return -1


def get_data():
    N = int(input())
    maze = list(map(int,input().split()))

    return [N, maze]


if __name__ == "__main__":
    N, maze = get_data()
    start_point = 0
    end_point = N-1

    result = solution()

    print(result)