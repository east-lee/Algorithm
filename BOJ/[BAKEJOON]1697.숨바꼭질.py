def main(m,k):
    check = [0]*(2*k+1)
    q, new_q = [m], []
    cnt = 0
    while q:
        p = q.pop()
        if not check[p]:
            if p == k:
                break
            if 0<=(p+1)<2*k+1:
                new_q.append(p+1)
            if 0<=(p-1)<2*k+1:
                new_q.append(p-1)
            if 0<=(p*2)<2*k+1:
                new_q.append(p*2)
            check[p] = 1

        if not q and new_q:
            q = new_q
            new_q = []
            cnt +=1
    return cnt


if __name__ == "__main__":
    n, k = map(int,input().split())
    if n>=k:
        print(n-k)
    else:
        print(main(n, k))