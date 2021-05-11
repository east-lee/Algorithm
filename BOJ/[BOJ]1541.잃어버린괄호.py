def main(arr):
    result = 0
    if '+' in arr[0]:
        result = sum_arr(arr[0])
    else:
        result = int(arr[0])

    for i in range(1,len(arr)):
        if '+' in arr[i]:
            result -= sum_arr(arr[i])
        else:
            result -= int(arr[i])
    print(result)

def sum_arr(arr):
    arr = list(arr.split('+'))
    result = 0
    for i in arr:
        result += int(i)
    return result

if __name__ == "__main__":
    arr = input()
    main(arr.split("-"))