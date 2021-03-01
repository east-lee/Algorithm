for t in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    reach_time = sorted(list(map(int, input().split())))

    result="Possible"
    
    
    for index, i in enumerate(reach_time):
        if (i//M ) * K - len(reach_time[:index+1]) < 0:
            result='Impossible'
            break
    print(f'#{t} {result}')