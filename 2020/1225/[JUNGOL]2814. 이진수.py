for _ in range(10):
    arr = str(input())
    arr = arr[::-1]

    result = 0

    for idx, i in enumerate(arr):
        x = 2**idx
        result += int(i) * x
    print(result)