def solution(gems):
    answer = []
    len_check = list(set(gems))
    n = len(len_check)
    result = len(gems)
    for i in range(len(gems)-n+1):
        for j in range(i+n,len(gems)+1):
            start, end = i,j
            check_arr = gems[i:j]
            check_dir = {}
            if (j-i) > result:
                break

            for m in check_arr:
                if m in check_dir:
                    continue
                else:
                    check_dir[m] = 1

            if len(check_dir) == n and result>len(check_dir):
                print(check_arr,check_dir)
                result =end-start
                answer = [start+1,end]
                break



    print(answer)
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)