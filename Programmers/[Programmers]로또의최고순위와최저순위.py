def solution(lottos, win_nums):
    answer = []
    
    ranking = {'6':1,'5':2,'4':3,'3':4,'2':5,'1':6,'0':6}
    
    lottos.sort()
    win_nums.sort()
    
    matching_cnt = 0
    unknown_cnt = 0
    
    for i in range(6):
        if lottos[i] == 0: unknown_cnt += 1
    
    for i in range(6):
        for j in range(6):
            if lottos[i] == win_nums[j]:
                matching_cnt += 1
                break
    
    max_result = unknown_cnt + matching_cnt
    min_result = matching_cnt
    
    answer.append(ranking[str(max_result)])
    answer.append(ranking[str(min_result)])
    
    return answer