for _ in range(10):
    n = int(input())
    result = list([0]*n for _ in range(n))
    for k in range(1,n**2+1):
        if not k%n:
            i = n-1
            j = k//n-1
        else:
            i = k%n-1
            j = k // n
        result[i][j] = k
    for i in range(n):
        for j in range(n):
            print(result[i][j],end=' ')
        print()

