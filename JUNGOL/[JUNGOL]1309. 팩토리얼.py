testing = True
while testing:
    n = int(input())
    if not n:
        break
    result = 1
    for i in range(n,0,-1):
        if i != 1:
            print('{}! = {} * {}!'.format(i,i,i-1))
        else:
            print('{}! = {}'.format(i,i))
        result *= i
    print(result)