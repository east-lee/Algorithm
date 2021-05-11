def solution(n, weak, dist):
    answer = 0
    check_point = [0]*n
    dist.sort(reverse=True)
    for i in weak: check_point[i] = -1
    pos = False
    # dist가 가장 큰 친쿠부터 돌게하자
    cnt = 0
    while cnt < len(dist):
        max_cnt = 0
        result_list = []
        for i in range(n):
            if check_point[i] == -1:
                # reverse방향
                check_cnt = 0
                new_point = check_point[:]
                for j in range(dist[cnt]+1):
                    i = i-j
                    if i < 0:
                        i += n
                    if check_point[i] == -1:
                        new_point[i] = 0
                        check_cnt +=1
                if max_cnt < check_cnt:
                    max_cnt = check_cnt
                    result_list.append(new_point)

                # 정방향
                check_cnt = 0
                new_point = check_point[:]
                for j in range(dist[cnt]+1):
                    i = i+j
                    if i >= n: i -= n
                    if check_point[i] == -1:
                        new_point[i]=0
                        check_cnt +=1
                if max_cnt <check_cnt:
                    max_cnt = check_cnt
                    result_list.append(new_point)

        check_point = result_list[-1][:]
        cnt +=1

        if check_point == [0]*n:
            pos =  True
            break


    if pos: answer = cnt
    else: answer = -1




    return answer



n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n,weak,dist))