for _ in range(10):
    n = int(input())
    arr = list(['']*n for _ in range(n))
    chr_num = 65
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if chr_num >90:
                chr_num = 65
            arr[j][i]=chr(chr_num)
            chr_num+=1
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
