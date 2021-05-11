for _ in range(10):

    n,m = map(int,input().split())

    if m == 1:
        for i in range(1,n+1):
            for _ in range(n):
                print(i, end = ' ')
            print()
    elif m == 2:
        for i in range(n):
            if not i%2:
                for j in range(1,n+1):
                    print(j,end=' ')
            else:
                for j in range(n,0,-1):
                    print(j,end=' ')
            print()
    else:
        for i in range(1,n+1):
            for j in range(1,n+1):
                print(i*j, end =' ')
            print()