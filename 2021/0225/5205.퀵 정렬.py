def f(l,r):
    global arr,N
    if (r-l) < 1:
        return
    p = arr[l]
    i = l+1
    j = r
    while i<=j:
        while i<r+1 and arr[i] <= p:
            i += 1
        while j>=l+1 and arr[j] >= p:
            j -= 1
        if i<j:
            arr[i],arr[j]= arr[j],arr[i]

    arr[l],arr[j] = arr[j],arr[l]
    if j == N//2:
        return
    elif j < N//2:
        f(j + 1, r)
    else:
        f(l,j-1)



T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    f(0,N-1)
    print(f'#{t} {arr[N//2]}')