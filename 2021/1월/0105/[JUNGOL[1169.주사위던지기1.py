# M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
# M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
# M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
def f(k,r):
    global result
    if k==n:
        result.append(r)
        return 0

    for i in range(1,7):
        rr = r[:]
        rr.append(i)
        f(k+1,rr)
def f1(k,r):
    global result
    if k == n:
        result.append(r)
        return 0
    for i in range(1,7):
        rr = r[:]
        if i not in rr:
            rr.append(i)
            f1(k+1,rr)



testing = True
while testing:
    input_data = input()
    if not input_data: break
    n,m=map(int,input_data.split())
    if m !=3:
        result = []
        f(0,[])
        if m == 1:
            for i in result:
                for j in i:
                    print(j,end=' ')
                print()
        elif m == 2:
            print_result = []
            for i in result:
                ii = i[:]
                i.sort()
                if i in print_result:
                    pass
                else:
                    print_result.append(i)
                    for j in ii:
                        print(j,end=' ')
                    print()
    else:
        result = []
        f1(0,[])
        for i in result:
            for j in i:
                print(j,end= ' ')
            print()



