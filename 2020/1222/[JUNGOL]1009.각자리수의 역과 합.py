for _ in range(10):
    arr= []
    for _ in range(10):
        i = int(input())
        arr.append(i)
        if not i:
            arr.pop()
            break
    for i in arr:
        i = str(i)[::-1]
        result = 0
        for j in i:
            result += int(j)
        print(f'{int(i)} {result}')

