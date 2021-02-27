for _ in range(10):
    a = int(input())
    b = int(input())
    c = int(input())
    result = str(a*b*c)
    for i in range(10):
        p = 0
        for j in result:
            if i==int(j):
                p += 1
        print(p)
