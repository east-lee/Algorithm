from collections import deque


def main():
    cnt = 0

    dq = deque()
    dq.append([0,0])

    while dq:
        y,x = dq.popleft()

        if y == (M-1) and x == (N-1):
            cnt += 1
            continue

        for k in range(4):
            i,j = y+direction[k][0], x+direction[k][1]
            if 0<=i<M and 0<=j<N and arr[i][j] < arr[y][x]:
                dq.append([i,j])
    return cnt


direction = [[-1,0],[1,0],[0,-1],[0,1]]

if __name__ == "__main__":
    M, N = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(M))
    result = main()

    print(result)