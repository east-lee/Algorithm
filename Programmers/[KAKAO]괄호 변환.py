
answer = ''
def solution(p):
    global answer
    dividing(p)
    return answer

def dividing(arr):
    global answer
    num1,num2 = 0,0
    cnt = 0
    for i in arr:
        if i=='(':num1+=1
        else: num2+=1
        cnt +=1
        if num1==num2:
            u = arr[:cnt]
            v = arr[cnt:]
            break
    if check(u):
        answer+=u
        if not v:
            pass
        elif check(v):
            answer+= v
        else:
            dividing(v)

    else:
        answer += '('
        if check(v):
            answer+= v
        else:
            dividing(v)
        answer += ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('



def check(arr):

    q = []
    for i in arr:
        if i == '(':
            q.append(i)
        elif q and q[-1]=='(':
            q.pop()
        else:
            q.append('asdf')
            break
    if not q:
        return True
    else:
        return False

print(solution("()))((()"))