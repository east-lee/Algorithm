def solution(q,check,arr):
    new_q = []
    cnt = 1
    if not q: return 0
    while q:
        y,x = q.pop()
        for k in range(4):
            ny, nx = y+direction[k][0],x+direction[k][1]
            if 0<=ny<len(check) and 0<=nx<len(check[0]) and arr[ny][nx] == 0 and check[ny][nx] == 0:
                check[ny][nx] = 1
                arr[ny][nx] = cnt
                new_q.append([ny,nx])
        if cnt == -1:
            break
        if not q and new_q:
            q = new_q[:]
            new_q = []
            cnt += 1
    cnt -= 1
    for i in range(len(check)):
        for j in range(len(check[0])):
            if not arr[i][j]:
                cnt = -1
                break
        if cnt == -1:
            break
    # for i in arr:
    #     print(i)
    return cnt

direction = [[-1,0],[1,0],[0,-1],[0,1]]

def main(n,m):
    arr = list(list(map(int,input().split())) for _ in range(n))
    check = list([0]*m for _ in range(n))
    q = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                check[i][j] = 1
                arr[i][j] = 'start'
                q.append([i,j])

    print(solution(q,check,arr))

if __name__=='__main__':
    M, N = map(int,input().split())
    main(N,M)