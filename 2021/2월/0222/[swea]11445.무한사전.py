T = int(input())
for t in range(1,T+1):
    p, q = [input() for _ in range(2)]
    result = 'Y'
    if len(p)+1==len(q) and q[-1]=='a':
        result = 'N'
    print(f'#{t} {result}')
