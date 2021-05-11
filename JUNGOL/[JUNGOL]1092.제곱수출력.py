testing = True
while testing:
    data = input()
    if not data:break
    x,y = map(int,data.split())
    k = 20091024
    x = x%k
    arr=[]
    check = True
    cnt = 0
    while check or cnt <=y:
        cnt += 1
        x= x**2
        m = x%k
        if m not in arr: arr.append(m)
        else:
            cnt -= 1
            break
    u = y % len(arr)
    print(arr[u])