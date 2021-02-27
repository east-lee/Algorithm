for t in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    reach_time = sorted(list(map(int, input().split())))
    max_reach_time = reach_time[-1]
    result="Possible"
    bread = [0]*(max_reach_time+1)

    for index, i in enumerate(bread):
        if index != 0 and index % M == 0:
            for k in range(index,max_reach_time+1):
                bread[k] += K

    for i in reach_time: 
        bread[i] -= 1
        if bread[i] <0:
            result ="Impossible"
            break
        else:
            for k in range(i+1,max_reach_time+1):
                
                if bread[k]<0:
                    result ="Impossible"
                    break

    print(f'#{t} {result}')