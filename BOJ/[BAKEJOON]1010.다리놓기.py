def fact(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result



for _ in range(int(input())):
    n,m=map(int,input().split())
    result = fact(m)/(fact(m-n)*fact(n))
    print(int(result))

