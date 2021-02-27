testing = True
while testing:
    arr = input()
    if not arr:
        break
    koi_num = 0
    ioi_num = 0
    for i in range(len(arr)-2):
        if arr[i] == 'K' and arr[i:i+3] == 'KOI':
            koi_num +=1
        if arr[i] == 'I' and arr[i:i+3] == 'IOI':
            ioi_num +=1
    print(koi_num)
    print(ioi_num)