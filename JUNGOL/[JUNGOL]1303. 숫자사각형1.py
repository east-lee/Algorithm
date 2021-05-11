for _ in range(10):
    h, w = map(int,input().split())
    for i in range(1,h*w+1):
        print(i,end=' ')
        if not i%w:
            print()