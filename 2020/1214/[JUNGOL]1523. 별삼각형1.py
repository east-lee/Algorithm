for _ in range(10):
    n, m = map(int,input().split())
    result = 'INPUT ERROR!'
    if n<1 or n>100:
        print(result)
    else:
        if m == 1:
            print_result = [['']*n for _ in range(n)]
            cnt = 0
            while cnt < n:
                cnt += 1
                for i in range(cnt):
                    print_result[cnt-1][i] = '*'
                result = print_result
        elif m == 2:
            print_result = [['']*n for _ in range(n)]
            cnt = 0
            while cnt < n :
                cnt += 1
                for i in range(n-cnt+1):
                    print_result[cnt-1][i] = '*'
                result = print_result
        elif m == 3:
            x = 2*n - 1
            print_result = [[''] * x for _ in range(n)]
            start_x = 0
            start_y = n-1
            cnt = n
            while cnt > 0 :
                for i in range(2*cnt - 1):
                    print_result[cnt-1][start_x+i] = '*'
                start_x += 1
                start_y -= 1
                cnt -= 1
            result = print_result
        else:
            print('INPUT ERROR!')
    if type(result)!=str:
        for i in range(n):
            for j in range(len(result[i])):
                if not result[i][j]:
                    print(' ',end='')
                else:
                    print(result[i][j],end='')
            print()

