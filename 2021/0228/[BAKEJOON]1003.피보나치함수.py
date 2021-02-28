for _ in range(int(input())):
    N = int(input())
    call_zero = [0]*41
    call_one = [0]*41
    call_zero[0] = 1
    call_zero[1] = 0
    call_one[0] = 0
    call_one[1] = 1
    for i in range(2,41):
        call_zero[i] = call_zero[i-1] + call_zero[i-2]
        call_one[i] = call_one[i-1] + call_one[i-2]
    print(f'{call_zero[N]} {call_one[N]}')