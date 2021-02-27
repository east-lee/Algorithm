for _ in range(10):
    n = int(input())

    if 0<n<100 and n%2:
        check_list = [0]*n
        for i in range(1,n+1):
            if i <= n//2+1:
                x = 2*i-1
                print_result = '*'*x
                check_list[i] = print_result
                for _ in range(i-1):
                    print(' ',end='')
                print(print_result)
            else:
                print_result = check_list[i-2*(i-n//2-1)]

                for _ in range(i-2*(i-n//2-1)-1):
                    print(' ',end='')
                print(print_result)

    else:
        print('INPUT ERROR!')