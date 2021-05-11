def solution(words, queries):
    answer = []
    for i in queries:
        n = len(i)
        front_cnt = 0
        back_cnt = 0
        result = 0
        if i[0]=='?':
            front_cnt = i.count('?')
        else:
            back_cnt = i.count('?')
        for j in words:
            if len(j) == n:
                if front_cnt and i[front_cnt:] == j[front_cnt:]:
                    result +=1
                elif back_cnt and i[:-back_cnt]==j[:-back_cnt]:
                    result += 1
        answer.append(result)







    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))