T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    result = 'OFF'
    m_binary = ''
    while True:
        m_binary += str(M % 2)
        M = M//2
        if M <2:
            break
    check_part = m_binary[:N]
    if '0' not in check_part:
        result = 'ON'
    print(f'#{t} {result}')
