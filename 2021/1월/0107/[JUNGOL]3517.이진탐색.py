testing = True
while testing:
    n = int(input())
    if not n: break
    arr = list(map(int,input().split()))
    q = int(input())
    check_arr = list(map(int,input().split()))
    for i in check_arr:
        cc = False
        for idx,j in enumerate(arr):
            if i==j:
                print(idx,end=' ')
                cc = True
                break
        if not cc:
            print(-1,end=' ')
    print()