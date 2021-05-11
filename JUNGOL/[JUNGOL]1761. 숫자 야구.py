for _ in range(10):
    n = int(input())
    arrs = list(list(map(int,input().split())) for _ in range(n))
    result = []

    for i in range(123,1000):
        num = list(set(list(str(i))))
        checking = 0
        if len(num) == 3 and '0' not in num:
            checking_num = list(str(i))
            for arr in arrs:
                strike = 0
                ball = 0
                answer_num = list(str(arr[0]))

                for k in range(3):
                    if checking_num[k] == answer_num[k]:
                        strike += 1
                    elif checking_num[k] in answer_num:
                        ball += 1
                if strike == arr[1] and ball == arr[2]:
                    checking += 1
        if checking == n:
            result.append(i)
    print(len(result))

