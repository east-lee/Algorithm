for _ in range(10):
    s,e = map(int,input().split())
    print_result = []

    if s < e:
        for i in range(s,e+1):
            print_result.append(i)
    else:
        for i in range(s,e-1,-1):
            print_result.append(i)

    for j in print_result:
        for i in range(1,10):
            if i*j>=10:
                print(f'{j} * {i} = {i*j}',end='   ')
            else:
                print(f'{j} * {i} =  {i*j}',end='   ')
            if not i%3:
                print()
        print()
