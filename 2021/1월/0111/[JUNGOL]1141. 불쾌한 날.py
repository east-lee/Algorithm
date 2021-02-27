testing = True
while testing:
    n = int(input())
    if not n: break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    result = 0
    for i in range(n-1):
        my_height = arr[i]
        for j in range(i+1,n):
            if my_height <= arr[j]:
                break
            else:
                result +=1
    print(result)
