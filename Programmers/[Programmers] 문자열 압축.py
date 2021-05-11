def solution(s):
    n = len(s)
    answer = n
    for i in range(1,n+1):

        new_s = ''
        cnt = 1
        last_str = ''
        for j in range(n//i+1):
            k = j*i
            check_str = s[k:k+i]
            if k+i > n:
                check_str = s[k:]
            if not last_str:
                last_str = check_str
                cnt =1
            else:
                if last_str == check_str:
                    cnt +=1
                else:
                    if cnt == 1:
                        new_s += last_str
                    else:
                        new_s += str(cnt)
                        new_s += last_str
                        cnt = 1
                    last_str = check_str
        if cnt == 1:
            new_s += last_str
        else:
            new_s += str(cnt) + last_str
        if len(new_s)<answer:

            answer = len(new_s)

    return answer


# s_arr = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
s_arr = ["abcabcdede"]
for i in s_arr:
    print(solution(i))