T = int(input())
for t in range(1,T+1):
    N, A, B = map(int,input().split())
    max_result = min(A,B)
    min_result = A+B-N
    if min_result < 0:
        min_result = 0
    print(f'#{t} {max_result} {min_result}')

