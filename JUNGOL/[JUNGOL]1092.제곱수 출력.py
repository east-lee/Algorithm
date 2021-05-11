testing = True
while testing:
    data = input()
    if not data:break
    x,y = map(int,data.split())
    k=20091024
    last = []
    while y>1:
        if y%2:
            y = y-1
            last.append(x)
        else:
            y = y//2
            x = x**2
    for i in last:
        x *= i
    if x >k:
        x = x%k
    print(x%k)



