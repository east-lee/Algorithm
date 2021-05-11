for _ in range(10):
    n = int(input())
    arr = list([0]*n for _ in range(n))
    y, x = 0, n//2
    cnt = 0
    while cnt < n**2:

        if 0>y:
            y = n-1
        if 0>x:
            x = n-1
        cnt +=1
        arr[y][x] = cnt
        if cnt % n:
            y -= 1
            x -=1
        else:
            y+=1
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end= ' ' )
        print()
