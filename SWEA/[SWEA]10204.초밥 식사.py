T = int(input())
for t in range(1,T+1):
    n = int(input())
    checking = [0]*n
    a, b = [], []
    for _ in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a_score, b_score = 0,0
    cnt = 0
    while cnt < n:
        max_a, max_b = 0,0
        max_list_a,max_list_b = [],[]
        for i in range(n):
            if checking[i]: continue

            if max_a < a[i]:
                max_a = a[i]
                max_list_a = [i]
            elif max_a == a[i]: max_list_a.append(i)
            if max_b < b[i]:
                max_b = b[i]
                max_list_b = [i]
            elif max_b == b[i]: max_list_b.append(i)
        select_idx = 0
        if cnt% 2 == 0: #정연이 행복도선택
            max_b_check = 0

            for i in max_list_a:
                if max_b_check < b[i]:
                    max_b_check = b[i]
                    select_idx = i
            checking[i] = 1
            a_score += a[i]
        else:
            max_a_check = 0
            for i in max_list_b:
                if max_a_check < a[i]:
                    max_a_check = a[i]
                    select_idx = i
            checking[i] = 1
            b_score += b[i]
        cnt += 1
    print(f'#{t} {a_score-b_score}')
