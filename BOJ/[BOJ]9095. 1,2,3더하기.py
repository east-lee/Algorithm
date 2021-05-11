def solution(k,n):
    global result
    if k>n:
        return
    elif k == n:
        result += 1
        return
    solution(k+1,n)
    solution(k+2,n)
    solution(k+3,n)

T = int(input())
for t in range(T):
    n=int(input())
    result = 0
    solution(0,n)
    print(result)