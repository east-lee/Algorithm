for _ in range(10):
    n, m = map(int,input().split())

    if n<1 or n>99 or not n%2 or m<1 or m>3:
        print('INPUT ERROR!')
    else:
        if m == 1:
            result = list([-1]*n for _ in range(n))
            start_x, start_y = 0, 0
            cnt = 0
            num = 0
            j,i=0,0
            while cnt < n:
                while 0<=i and 0<=j:
                    num += 1
                    result[i][j] = num
                    j -= 1

                start_x += 1
                start_y += 1
                i,j=start_x,start_y
                cnt += 1
            for i in range(n):
                if not i % 2:
                    result[i] = result[i][:i+1]
                    result[i] = result[i][::-1]

        elif m==2:
            result = list([-1]*(2*n-1) for _ in range(n))
            cnt = 0
            while cnt < n:
                for j in range(cnt,len(result[0])-cnt):
                    result[cnt][j] = cnt
                cnt +=1
        else:
            result = list([-1]*n for _ in range(n))
            c = 0
            for i in range(n):
                if i<=n//2:
                    cnt = 1
                    for j in range(c+1):
                       result[i][j] = cnt
                       cnt += 1
                    c += 1
                else:
                    c -=1
                    cnt = 1
                    for j in range(c):
                        result[i][j] = cnt
                        cnt += 1
        for i in range(n):
            for j in range(len(result[i])):
                if result[i][j]!=-1:
                    print(result[i][j],end = ' ')
                else:
                    print(' ',end=' ')
            print()
