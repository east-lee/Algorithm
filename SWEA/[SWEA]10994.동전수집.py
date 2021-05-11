def solution(now_price,he_have):
    global result,result_price,K
    check_list = he_have[:]
    change=K-now_price
    while change:
        for i in range(change,0,-1):
            if is_exist[i] and i<=change:
                change-=i
                check_list[i] = 1
                break
    check_num = check_list.count(1)
    if check_num > result:
        result = check_num
        result_price=now_price
    # print(check_list,now_price)

T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    is_exist = [0]*(K+1)
    he_have = [0]*(K+1)
    result = 0
    result_price = 0

    for _ in range(N):
        c,d = map(int,input().split())
        he_have[c]=d
        is_exist[c] = 1

    for i in range(K-1,0,-1):
        solution(i,he_have)
    print(f'#{t} {result-he_have.count(1)} {result_price}')