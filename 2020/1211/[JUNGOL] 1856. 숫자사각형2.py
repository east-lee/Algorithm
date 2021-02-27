for _ in range(10):
    h,w= map(int,input().split())
    print_result = []
    for i in range(1,h*w+1):
        if len(print_result) <= w:
            print_result.append(i)
        if not i % w:
            if not (i//w)%2:
                print_result = print_result[::-1]
            for j in print_result:
                print(j,end=' ')
            print()
            print_result = []

