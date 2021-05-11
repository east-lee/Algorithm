def check(str):
    cnt_aeiou= 0
    cnt_else = 0
    for i in str:
        if i in aeiou:
            cnt_aeiou += 1
        else:
            cnt_else += 1
    if cnt_aeiou >= 1 and cnt_else >= 2:
        return True
    else:
        return False

def main(k,result,check_list):
    global result_list
    if k == L:
        if check(result):
            result_list.append(result)
    for i in range(k,C):
        if i not in check_list and (not check_list or check_list[-1] < i):
            result += arr[i]
            check_list.append(i)
            main(k+1,result, check_list)
            check_list.pop()
            result = result[:-1]
        else:
            continue


if __name__ == "__main__":
    L, C = map(int,input().split())
    arr = list(map(str,input().split()))
    arr.sort()
    aeiou = "aeiou"
    result_list = []
    main(0,"",[])
    for i in result_list:
        print(i)