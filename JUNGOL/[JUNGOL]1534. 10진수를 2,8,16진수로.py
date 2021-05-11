for _ in range(10):
    n, x = map(int,input().split())
    result = ''
    arr = ['A', 'B', 'C', 'D', 'E', 'F']
    while n > 0:
        y = n%x
        if y >= 10:
            y = arr[y-10]
        n = n//x
        result += str(y)
    print(result[::-1])



