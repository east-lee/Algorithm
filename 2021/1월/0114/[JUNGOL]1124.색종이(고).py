def bfs(y,x):
    row = 0
    cnt = 0
    for i in range(y,100):
        cnt_cnt = 0
        for j in range(x,100):
            if arr[i][j]==1:
                cnt_cnt += 1
            else:
                break

testing = True
while testing:
    n = int(input())
    if not n: break
    arr = list([0]*100 for _ in range(100))
    for _ in range(n):
        a,b = map(int,input().split())
        for i in range(a,a+10):
            for j in range(b,b+10):
                arr[i][j] = 1
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    result = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                bfs(i,j)


