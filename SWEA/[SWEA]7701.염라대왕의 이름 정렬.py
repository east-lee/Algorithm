T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = []
    max_len = 0
    for _ in range(n):
        input_num = input()
        if len(input_num) > max_len: max_len = len(input_num)
        arr.append(input_num)

    arr = list(set(arr))
    arr.sort(key=lambda x : len(x))
    for i in range(max_len):
        try:
            arr.sort(key=lambda x:x[i])
        except:
            continue

    print(f'#{t}')
    for i in arr:
        print(i)