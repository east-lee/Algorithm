def solution(y,x):
    global arr
    arr[y][x] = 0
    q = [[y,x]]
    while q:
        i,j = q.pop()
        for k in range(8):
            ni,nj = i+direction[k][0], j+direction[k][1]
            if 0<=nj<w and 0<=ni<h and arr[ni][nj]:
                arr[ni][nj] = 0
                q.append([ni,nj])



direction = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
while True:
    w,h = map(int,input().split())
    if not w and not h: break
    arr = []
    for _ in range(h):
        arr.append(list(map(int,input().split())))
    result = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                result += 1
                solution(i,j)

    print(result)