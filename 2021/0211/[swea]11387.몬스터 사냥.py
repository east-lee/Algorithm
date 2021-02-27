T = int(input())

for t in range(1,T+1):
    D, L, N = map(int,input().split())
    D = D//100
    cnt, result = 0, 0
    while cnt < N:
        result += 100*D + D*cnt*L
        cnt += 1
    print(f'#{t} {result}')