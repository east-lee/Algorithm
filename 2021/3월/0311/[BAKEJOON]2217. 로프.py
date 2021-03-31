def main(arr):
    arr.sort(reverse=True)
    result = [0]*len(arr)
    max_result = 0
    for i in range(n):
        result[i] = arr[i] * (i+1)
        if result[i] > max_result:
            max_result = result[i]
    print(max_result)


if __name__ == "__main__":
    n = int(input())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())
    main(arr)