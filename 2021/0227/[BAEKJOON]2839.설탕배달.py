# 설탕을 담을 수 있는 봉지: 3kg / 5kg -> 최대한 적은양의 봉지
N = int(input())
result = 0
if not N%5:
    result = N//5
else:
    cnt = 0
    breaker = False
    while N%5:
        if N < 0:
            breaker = True
            break
        cnt += 1
        N -= 3
        result += 1
    if breaker:
        result = -1
    else:
        result += N//5
print(result)

