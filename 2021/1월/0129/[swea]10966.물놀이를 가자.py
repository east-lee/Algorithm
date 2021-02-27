T = int(input())
for t in range(1,T+1):
    h,w = map(int,input().split())
    arr = list(input() for _ in range(h))
    check = list([0]*w for _ in range(h))

    q = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'W':
                q.append([i,j])
    new_q=[]
    cnt = 1
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    result = 0
    while q:
        
        y,x = q.pop()
        for k in range(4):
            i,j = y+direction[k][0],x+direction[k][1]
            if 0<=i<h and 0<=j<w and arr[i][j] == 'L' and check[i][j] == 0:
                check[i][j] = cnt
                result += cnt
                new_q.append([i,j])
        if not q and new_q:
            cnt += 1
            q=new_q
            new_q=[]
    print(f'#{t} {result}')