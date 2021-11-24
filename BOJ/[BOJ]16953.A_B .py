from collections import deque

def solution():
    # global visited

    dq = deque()
    dq.append([A, 0])

    while dq:
        num, cnt = dq.popleft()
        # if visited[num]: continue
        if num == B:
            return cnt+1

        num_a, num_b = num * 2, int(str(num)+'1')
        # visited[num] = True

        if num_a <= B:
            dq.append([num_a, cnt+1])
        if num_b <= B:
            dq.append([num_b, cnt+1])

    return -1



def get_data():
    A, B = map(int, input().split())

    return [A, B]

if __name__ == "__main__":
    A, B = get_data()
    # visited = [False] * (B+1)
    result = solution()

    print(result) if result != -1 else print(-1)

