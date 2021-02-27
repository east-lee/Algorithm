for _ in range(10):
    n = int(input())
    if 1<=n<=100 and n%2:
        start_y = start_x  = y = x = n//2
        chr_num =  65
        arr = list(['']*n for _ in range(n))
        num = 0
        idx_num = 0
        while start_x >= 0:
            num += 1
            if chr_num > 90: chr_num = 65

            arr[y][x] = chr(chr_num)

            y += 1
            if y>=n or num == idx_num*2+1:
                idx_num += 1
                num = 0
                start_x -= 1
                start_y -= 1
                y = start_y
                x = start_x
            chr_num+=1
        for i in range(n):
            for j in range(n):
                if arr[i][j]:
                    print(arr[i][j],end = ' ')
                else:
                    print(' ',end = ' ')
            print()
    else:
        print('INPUT ERROR')