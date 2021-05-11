T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    result = 0
    for i in range(N):
        for j in range(i+1,N):
            a,b = arr[i]
            c,d = arr[j]
            if a > c and b<d:
                result += 1
            elif a <c and b>d:
                result += 1
    print(f'#{t} {result}')
