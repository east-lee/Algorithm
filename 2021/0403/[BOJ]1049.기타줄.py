if __name__ == "__main__":
    N, M = map(int,input().split())

    min_cost = [10000,10000]

    for _ in range(M):
        six_cost, one_cost = map(int,input().split())
        min_cost[0],min_cost[1] = min(min_cost[0],six_cost),min(min_cost[1],one_cost)
    
    cnt = 0
    min_result = 100000000000000000
    while cnt < N//6+2:
        
        if N-cnt*6 >0:
            cost = cnt*min_cost[0] + (N-cnt*6)*min_cost[1]
        else:
            cost = cnt*min_cost[0]
        if cost < min_result:
            min_result = cost
        cnt+=1
    
    print(min_result)