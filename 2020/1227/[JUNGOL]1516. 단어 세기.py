for _ in range(10):
    testing = True
    while testing:
        arr = list(map(str,input().split()))
        if arr == ['END']:
            break
        else:
            arr_dict = {}
            for i in arr:
                if i not in arr_dict:
                    arr_dict[i] = 1
                else:
                    arr_dict[i] += 1
            result = []
            for key, value in arr_dict.items():
                result.append(f'{key} : {value}')
            result.sort()
            for i in result:
                print(i)