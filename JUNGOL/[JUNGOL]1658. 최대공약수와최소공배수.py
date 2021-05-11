for _ in range(10):
    n,m = map(int,input().split())
    x = min(n,m)
    y = max(n,m)
    result = 0
    for i in range(1,x+1):
        if x%i == 0 and y%i==0:
            result = i
    print(result)
    print(result*(x//result)*(y//result))