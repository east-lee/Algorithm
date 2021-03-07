def solution(y,x):
    global arr
    q = []
    q.append([y,x])
    while q:
        i,j = q.pop()
        arr[i][j] = 0
        for k in range(4):
            next_i,next_j = i+direction[k][0],j+direction[k][1]
            if 0<=next_i<n and 0<=next_j<m and arr[next_i][next_j]:
                q.append([next_i,next_j])
                arr[next_i][next_j]=0


direction = [[1,0],[-1,0],[0,1],[0,-1]]
for _ in range(int(input())):
    m,n,k = map(int,input().split())
    arr = list([0]*m for _ in range(n))
    result = 0
    for _ in range(k):
        x,y = map(int,input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                result += 1
                solution(i,j)
    print(result)