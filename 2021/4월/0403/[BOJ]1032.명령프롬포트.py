if __name__ == "__main__":
    n = int(input())
    str_arr = []
    for _ in range(n):
        str_arr.append(input())
    
    result = ''

    for i in range(len(str_arr[0])):
        check_str = str_arr[0][i]
        breaker = False
        for j in range(n):
            if check_str != str_arr[j][i]:
                breaker = True
                break 
        if breaker:
            result += '?'
        else: result += check_str
    print(result)
