import math

T = int(input())
for t in range(1,T+1):
    a, b = map(int,input().split())
    result = 0
    for i in range(a,b+1):
        check_i = math.sqrt(i)
        str_check = str(int(check_i))
        str_i = str(i)
        if check_i == float(int(check_i)) and str_i == str_i[::-1] and str_check == str_check[::-1]:
            result+= 1
    print(f'#{t} {result}')
