T = int(input())
for t in range(1,T+1):
    L, N = (int(input()) for _ in range(2))
    checking = [0]*10**8
    max_ei = 0
    for _ in range(N):
        si,ei = map(int,input().split())
        for i in range(si,ei+1):
            checking[i] = 1
        if max_ei < ei:max_ei =ei
    result = 0

    for i in range(max_ei+1):
        start_time = i
        end_time = i+L
        check_time = checking[i+1:i+L-1]
        if result < sum(check_time):
            result = sum(check_time)
    print(f'#{t} {result}')
