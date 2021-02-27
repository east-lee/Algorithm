for t in range(1,int(input())+1):
    result = ''
    max_n = 0
    arr = []
    for _ in range(5):
        input_str = input()
        n = len(input_str)
        if n > max_n:max_n = n
        arr.append(input_str)

    check = list(['']*max_n for _ in range(5))

    for i in range(5):
        for j in range(len(arr[i])):
            check[i][j] = arr[i][j]
    for i in range(max_n):
        for j in range(5):
            result += check[j][i]
    print(f'#{t} {result}')