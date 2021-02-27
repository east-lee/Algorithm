T = int(input())
for t in range(1, T+1):
    arr = input()
    arr = arr[::-1]
    result = ''
    arr_dict = {'p':'q','q':'p','b':'d','d':'b'}
    for i in arr:
        result += arr_dict[f'{i}']
    print(f'#{t} {result}')