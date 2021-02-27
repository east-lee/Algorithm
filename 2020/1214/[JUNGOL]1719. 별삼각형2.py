for _ in range(10):
    n, m = map(int,input().split())

    if m<1 or m>4 or n<1 or n>100 or not n%2:
        print('INPUT ERROR!')
    else:
        result = [[''] * n for _ in range(n)]
        if m == 1:
            cnt = 0
            for i in range(n):
                if i <= n//2:
                    cnt += 1
                    for j in range(cnt):
                        result[i][j] = '*'
                else:
                    cnt -= 1
                    for j in range(cnt):
                        result[i][j] = '*'
        elif m == 2:
            result = list(['']*(n//2+1) for _ in range(n))
            cnt = 0
            for i in range(n):
                if i <= n//2:
                    cnt += 1
                    for j in range(n//2,n//2-cnt,-1):
                        result[i][j] = '*'
                else:
                    cnt -= 1
                    for j in range(n//2,n//2-cnt,-1):
                        result[i][j]='*'



        elif m == 3:
            cnt = 0
            for i in range(n):
                if n//2 > i:
                    for j in range(cnt,n-cnt):
                        result[i][j] = '*'
                    cnt += 1
                else:
                    for j in range(cnt,n-cnt):
                        result[i][j] = '*'
                    cnt -= 1
        else:
            cnt = 0
            revers_cnt = 1
            for i in range(n):
                if n//2 > i:
                    for j in range(cnt,n//2+1):
                        result[i][j] = '*'
                    cnt += 1
                else:
                    for j in range(n//2,n//2+revers_cnt):
                        result[i][j] = '*'
                    revers_cnt += 1
        for i in range(n):
            for j in range(len(result[0])):
                if result[i][j]:
                    print(result[i][j],end='')
                else:
                    print(' ',end='')

            print()
