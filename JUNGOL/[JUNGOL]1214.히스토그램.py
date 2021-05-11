TESTING=True
while TESTING:
    data = input()
    if not data: break
    arr = list(map(int,data.split()))
    result = 0
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            new_list = arr[i:j]
            if result < (j-i)*min(new_list):
                result = (j-i)*min(new_list)
    print(result)