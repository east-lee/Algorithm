T = int(input())

for t in range(1,T+1):
    s, p, q, m = map(int,input().split())
    check = [0]*10**6
    check[s],cnt,result = 1,1,0
    while True:
        cnt +=1
        next_s = ((p*s+q) % m)
        if check[next_s]:
            result = cnt-check[next_s]
            break
        else:
            check[next_s] = cnt
            s = next_s
    print(f'#{t} {result}')