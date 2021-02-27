testing = True
while testing:
    data = input()
    if not data: break
    n, p = map(int,data.split())
    arr= [n]
    check = False
    start_idx = 0
    while not check:
        x = (arr[-1]*n)%p
        if x in arr:
            for i in range(len(arr)):
                if arr[i]==x:
                    start_idx = i
            break
        arr.append(x)
    print(len(arr[start_idx:]))
    