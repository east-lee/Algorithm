T=10
for t in range(1,T+1):
    n = int(input())
    result = ''
    for i in range(1,n+1):
        check = str(i)
        for j in check:
            if int(j)%3==0 and int(j):
                result += '-'
            else:
                result += str(j)
        result += ' '
    print(result)