T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    checked = []
    result = 'Yes'
    for i in arr:
        if i > n or i<=0:
            result = 'No'
            break
        elif i in checked:
            result = 'No'
            break
        else:
            checked.append(i)
    print(f'#{t} {result}')