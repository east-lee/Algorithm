T= int(input())

for t in range(1,T+1):
    N = int(input())
    candy = list(map(int,input().split()))
    result= 0
    for i in range(1<<N):
        me, me_xor = [], 0
        you, you_xor = [], 0
        for j in range(N):
            if i & (1<<j):
                me.append(candy[j])
            else:
                you.append(candy[j])
        if result < sum(me) and me and you:
            for idx, i in enumerate(me):
                if idx == 0:
                    me_xor = me[idx]
                else:
                    me_xor = me_xor ^ me[idx]
            for idx, i in enumerate(you):
                if idx == 0: you_xor = you[idx]
                else: you_xor = you_xor ^ you[idx]
            if you_xor == me_xor: result = sum(me)


    if result:
        print(f'#{t} {result}')
    else:
        print(f'#{t} NO')
