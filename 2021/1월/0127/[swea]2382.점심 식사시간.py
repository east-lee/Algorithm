T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = list(list(map(int,input().split())) for _ in range(n))
    check_time = list([0]*n for _ in range(n))
    q = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]>1:
                q.append([i,j])
    new_q = []
    cnt = 1
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    while q:
        y, x =q.pop()
        for k in range(4):
            i,j=y+direction[k][0],x+direction[k][1]
            if 0<=i<n and 0<=j<n and arr[i][j]<=1 and check_time[i][j] == 0:
                check_time[i][j]=cnt
                new_q.append([i,j])
        if not q and new_q:
            q=new_q
            cnt += 1
    print(check_time)
