testing = True
while testing:
    data = input()
    if not data: break
    n,m = map(int,data.split())
    r,c,s,k = map(int,input().split())
    direction = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

    q = []
    q.append([r,c])
    next_q = []
    cnt = 1
    result=0
    breaker=False
    while q:
        y,x = q.pop()
        for k in range(8):
            next_y,next_x = y+direction[k][0],x+direction[k][1]
            if 0<=next_y<n and 0<=next_x<m:
                if next_y == s and next_x==k:
                    result = cnt
                    q= []
                    next_q=[]
                    breaker=True
                    break
                else:
                    next_q.append([next_y,next_x])
        if breaker:break
        if not q:
            q = next_q
            cnt +=1
    print(result)
