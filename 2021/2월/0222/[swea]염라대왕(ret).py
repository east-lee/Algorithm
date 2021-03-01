T = int(input())
for t in range(1,T+1):
    N = int(input())
    print(f'#{t}')

    arr = [input() for _ in range(N)]
    arr = list(set(arr))
    arr.sort()
    arr.sort(key=lambda x:len(x))
    for i in arr: print(i)