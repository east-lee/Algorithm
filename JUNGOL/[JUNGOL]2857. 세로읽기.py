testing = True
while testing:
    arr = list(list(map(str,input())) for _ in range(5))
    if not arr:
        break
    max_len = 0
    for i in arr:
        if max_len < len(i):
            max_len = len(i)

    result =''
    for i in range(max_len):
        for j in range(5):
            try:
                if arr[j][i]:
                    result += arr[j][i]
            except:
                pass
    print(result)
