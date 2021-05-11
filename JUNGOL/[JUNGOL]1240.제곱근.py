testing = True
while testing:
    n = int(input())
    if not n: break
    for i in range(1,n):
        if i**2<=n<(i+1)**2:
            print(i)
            break