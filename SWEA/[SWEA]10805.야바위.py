def dfs(k,done,ball_location):
    global result
    if k == q:
        if done:
            result[ball_location] = 1
        else:
            if ball_location + 1<n:
                result[ball_location + 1]= 1
            if ball_location - 1 >= 0:
                result[ball_location-1]=1
        return
    a, b = arr[k][0] - 1, arr[k][1] - 1
    if done:
        if ball_location == a: ball_location= b
        elif ball_location==b:ball_location=a
        dfs(k+1,done,ball_location)

    else:
        #firstcase
        if ball_location-1 >=0:
            next_ball = ball_location - 1
            if next_ball == a: next_ball = b
            elif next_ball == b : next_ball = a
            dfs(k+1,1,next_ball)
        if ball_location + 1<n:
            next_ball = ball_location + 1
            if next_ball == a:
                next_ball = b
            elif next_ball == b:
                next_ball = a
            dfs(k + 1, 1, next_ball)
        if ball_location == a: ball_location= b
        elif ball_location==b:ball_location=a
        dfs(k+1,done,ball_location)


T = int(input())

for t in range(1, T+1):
    n,q = map(int,input().split())
    arr = []
    for _ in range(q):
        arr.append(list(map(int,input().split())))
    result = [0]*n
    check = [0]*n
    check[0] = 1
    dfs(0,0,0)

    num = 0
    for i in result:
        if i:num+=1
    print(f'#{t} {num}')