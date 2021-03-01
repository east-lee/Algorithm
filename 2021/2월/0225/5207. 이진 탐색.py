def f(i,l,r):
    global cnt
    check = []
    m = (l + r) // 2
    while A[m] != i:
        # 오른쪽 구간
        if i > A[m]:
            l = m+1
            check.append('r')
        elif i < A[m]:
            r = m-1
            check.append('l')
        m = (l+r)//2
        if len(check)>=2 and check[-1] == check[-2]:
            return
    cnt += 1
T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    l, r = 0, len(A)-1
    cnt = 0
    for i in B:
        if i in A:
            f(i,l,r)

    print(f'#{t} {cnt}')