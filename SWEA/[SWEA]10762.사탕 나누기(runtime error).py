# xor > 달라야 1

def f(k,N,me,you,me_xor,you_xor):
    global pos
    if k == N:
        if you_xor == me_xor and me and you:
            pos = 1
            result.append(sum(me))
        return
    if me:
        me.append(candy[k])
        f(k+1,N,me,you,me_xor^candy[k],you_xor)
    else:
        me.append(candy[k])
        f(k + 1, N, me, you, candy[k], you_xor)
    a = me.pop()
    if you:
        you.append(a)
        f(k+1,N,me,you,me_xor,you_xor^a)
    else:
        you.append(a)
        f(k + 1, N, me, you, me_xor, a)
    you.pop()

T = int(input())

for t in range(1,T+1):
    N = int(input())
    candy = list(map(int,input().split()))
    pos = 0
    result=[]
    f(0,N,[],[],0,0)
    if pos:
        print(f'#{t} {max(result)}')
    else:
        print(f'#{t} N0')
