if __name__ == "__main__":
    N,k = int(input()), int(input())
    btn = [i for i in range(10)]
    if k > 0:
        breakdown = list(map(int,input().split()))
    else:
        breakdown = []
    check = [0]*(500000*2+1)
    min_result = abs(100-N)
    q = []
    new_q = []
    q.append(N)
    while q:
        p = q.pop()
        check[p] = 1
        if abs(N-p)>min_result:
            break
        cnt = 0
        for i in str(p):
            if int(i) not in breakdown:
                cnt += 1
            else: break
        if cnt == len(str(p)):
            break
        if p+1 < 500000*2+1 and check[p+1] == 0:
            new_q.append(p+1)
        if p-1 >= 0 and check[p-1] == 0:
            new_q.append(p-1)

        if not q and new_q:
            q = new_q
            new_q = []


    print(min(min_result,len(str(p))+abs(p-N)))