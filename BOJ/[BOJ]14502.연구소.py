import copy
direction = [[-1,0],[1,0],[0,-1],[0,1]]

def solution(arr):
    global min_result
    q = virus[:]
    result = 0
    while q:
        result += 1
        i,j = q.pop()
        for k in range(4):
            if 0<=i+direction[k][0]<N and 0<=j+direction[k][1]<M and arr[i+direction[k][0]][j+direction[k][1]] == 0:
                arr[i+direction[k][0]][j+direction[k][1]] = 2
                q.append([i+direction[k][0],j+direction[k][1]])
    if result < min_result:
        # for i in arr:
        #     print(i)
        min_result = result


def main(n,m,arr,k):
    if k == 3:
        solution(arr)
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                copy_arr = copy.deepcopy(arr)
                copy_arr[i][j] = 1
                main(n,m,copy_arr,k+1)


if __name__ == "__main__":
    N,M = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(N))
    virus = []
    min_result = N*M
    cnt = 3
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus.append([i,j])
            elif arr[i][j] == 1:
                cnt += 1
    main(N,M,arr,0)
    print(N*M-min_result-cnt)