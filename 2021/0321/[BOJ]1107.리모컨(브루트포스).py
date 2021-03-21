if __name__ == "__main__":
    N,M = list(int(input()) for _ in range(2))
    cant = []
    if M > 0:
        cant = list(map(str,input().split()))
    remote = [str(i) for i in range(10) if str(i) not in cant]
    result = abs(100-N)

    for i in range(1000001):
        check = True
        for j in str(i):
            if j not in remote:
                check = False
                break

        if check:
            result = min(result,len(str(i))+abs(N-i))

    print(result)