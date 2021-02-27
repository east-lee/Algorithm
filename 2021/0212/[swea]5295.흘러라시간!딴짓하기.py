from itertools import combinations


T = int(input())
for t in range(1,T+1):
    N = int(input())
    num_arr = [i for i in range(N)]
    arr = [list(map(int,input().split())) for _ in range(3)]

    breaker = False
    cnt = 0
    while cnt < N:
        cnt += 1
        combis = list(combinations(num_arr,cnt))
        for combi in combis:
            list_1 = []
            list_2 = []
            list_3 = []
            for i in range(N):
                if i not in combi:
                    list_1.append(arr[0][i])
                    list_2.append(arr[1][i])
                    list_3.append(arr[2][i])
            list_1.sort()
            list_2.sort()
            list_3.sort()

            if list_1 == list_2 and list_2==list_3:
                breaker = True
                break
        if breaker:break
    print(f'#{t} {cnt}')