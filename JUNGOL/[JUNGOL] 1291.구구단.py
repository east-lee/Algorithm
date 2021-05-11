for _ in range(10):
    s, e = map(int,input().split())
    print_result = []
    error_check = ''
    if s<e:
        for i in range(s,e+1):
            if 2<=i<=9:
                print_result.append(i)
            else:
                error_check = 'INPUT ERROR!'
                break

    else:
        for i in range(s,e-1,-1):
            if 2<=i<=9:
                print_result.append(i)
            else:
                error_check = 'INPUT ERROR!'
                break
    if error_check:
        print(error_check)
    else:
        for i in range(1,10):
            for idx,j in enumerate(print_result):
                if idx == len(print_result) -1:
                    if i * j >= 10:
                        print(f'{j} * {i} = {i * j}')
                    else:
                        print(f'{j} * {i} =  {i * j}')
                else:
                    if i*j >=10:
                        print(f'{j} * {i} = {i*j}', end='   ')
                    else:
                        print(f'{j} * {i} =  {i*j}', end='   ')
