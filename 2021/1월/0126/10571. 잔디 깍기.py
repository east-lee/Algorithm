def check(H, original, N, M):
    for i in range(M):
        for j in range(N):
            if H[i][j] != original[i][j]:
                return False
    return True


T = int(input())

for tc in range(1, T + 1):
    M, N = map(int, input().split())
    H = [list(map(int, input().split())) for _ in range(M)]
    original = [[100] * N for _ in range(M)]
    for i in range(M):
        max_num = max(H[i])
        for j in range(N):
            if original[i][j] > max_num:
                original[i][j] = max_num
    for i in range(N):
        max_num = 0
        for j in range(M):
            if H[j][i] > max_num:
                max_num = H[j][i]
        for j in range(M):
            if original[j][i] > max_num:
                original[j][i] = max_num
    if check(H, original, N, M):
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))