for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    testing = True
    cnt = 0
    while cnt <n-1:
        min_idx = -1
        min_value = 101
        for idx,i in enumerate(arr):
            if idx>=cnt and min_value > i:
                min_value = i
                min_idx = idx
        if min_idx != cnt:
            first = arr.pop(min_idx)
            last = arr.pop(cnt)
            arr.insert(cnt,first)
            arr.insert(min_idx,last)
        for i in arr:
            print(i,end=' ')
        print()
        cnt += 1





