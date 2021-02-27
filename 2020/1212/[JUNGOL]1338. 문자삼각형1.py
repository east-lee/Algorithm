for _ in range(10):
    n = int(input())
    arr = list(['']*n for _ in range(n))
    chr_num = 65
    y = 0
    x = n-1
    start_y = 0
    start_x = n-1
    while start_y<n:
        if chr_num > 90: chr_num=65
        arr[y][x] = chr(chr_num)
        y += 1
        x -=1
        if y<0 or y>=n or x<0 or x>=n:
            start_y +=1
            y = start_y
            x = start_x
        chr_num += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j],end = ' ')
            else:
                print(' ', end= ' ')
        print()