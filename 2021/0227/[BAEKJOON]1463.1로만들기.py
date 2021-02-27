N = int(input())
check = [0 for _ in range(N+1)]

for i in range(1,N+1):
    if i == 1:
        check[i] = 0
        continue
    check[i] = check[i-1] + 1

    if not (i)%3:
        div_by_3 = check[i//3]+1
        check[i] = min(check[i],div_by_3)
    elif not (i)%2:
        div_by_2 = check[i//2]+1
        check[i] = min(div_by_2,check[i])
print(check[-1])



