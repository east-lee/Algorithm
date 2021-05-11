testing = True
while testing:
    n = int(input())
    if not n: break
    arr = list([0]*101 for _ in range(101))
    for _ in range(n):
        left, right = map(int,input().split())
        for i in range(right,right+10):
            for j in range(left,left+10):
                arr[i][j] = 1
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    result = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                for k in range(4):
                    y, x = i+direction[k][0], j+direction[k][1]
                    if 0<=y<101 and 0<=x<101 and arr[y][x] != 1:
                        result += 1



    print(result)
