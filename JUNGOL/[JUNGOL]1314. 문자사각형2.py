for _ in range(10):
    chr_num = 65
    n = int(input())
    arr = list(['']*n for _ in range(n))
    check_num = 0
    d = [[1,0],[-1,0]]
    d_num = 0
    y,x = 0,0
    arr[y][x] = chr(chr_num)
    while check_num<n**2-1:
        check_num += 1
        chr_num+=1
        if chr_num >90: chr_num=65
        if y +d[d_num][0]<0 or y+d[d_num][0]>=n or x +d[d_num][1] < 0 or x +d[d_num][1]>=n:
            x += 1
            d_num = (d_num+1)%2
        else:
            y += d[d_num][0]
            x += d[d_num][1]
        arr[y][x] = chr(chr_num)
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()

