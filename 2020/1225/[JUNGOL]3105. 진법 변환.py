for _ in range(20):
    doing = True
    while doing:
        check =input()
        if check != '0':
            a, n ,b = map(str,check.split())
            a = int(a)
            b = int(b)
            arr = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            n = str(n)[::-1]
            first_result = 0
            for idx, i in enumerate(n):
                for jdx, j in enumerate(arr):
                    if j == i:
                        i = jdx+10
                        break
                x = a**idx
                first_result += x*int(i)
            result = ''
            if not first_result:
                result = '0'
            while first_result > 0:
                y = first_result % b
                if y >= 10:
                    y = arr[y-10]
                result += str(y)
                first_result = first_result //b


            print(result[::-1])
        else:
            doing = False

