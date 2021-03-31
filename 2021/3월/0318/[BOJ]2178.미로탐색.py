def main():
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    q = []
    check = [[0]*M for _ in range(N)]
    check[0][0] = 1
    q.append([0,0])
    result = 0
    cnt = 1
    new_q=[]
    while q:
        i,j= q.pop()
        for k in range(4):
            y,x = i+direction[k][0],j+direction[k][1]
            if 0<=y<N and 0<=x<M and arr[y][x] == "1" and check[y][x] == 0:
                check[y][x] = 1
                new_q.append([y,x])
                if y==N-1 and x == M-1:
                    cnt += 1
                    result = cnt
                    break
        if result:
            break
        if not q and new_q:
            q= new_q
            new_q = []
            cnt +=1
    return result


if __name__ == "__main__":
    N,M = map(int,input().split())
    arr = list(input() for _ in range(N))
    print(main())