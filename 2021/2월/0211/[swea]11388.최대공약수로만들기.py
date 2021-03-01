T = int(input())
for t in range(1,T+1):
    N, G = map(int,input().split())
    arr = list(map(int,input().split()))
    #check => G로 나눌수있는경우 // 0이면 있으면안됨
    check = [0]*N
    #check_2=> G의 두배수로 나누었을때도 가능함 -> check_2는1인거로만 이루어지면 안됨
    check_2 = [0]*N
    num = 0
    num2 = 0
    for i in range(N):
        if arr[i]>=G and arr[i]%G ==0:
            check[i] = 1
            num += 1
            if arr[i]//G != 1 and arr[i]//G >= G and (arr[i]//G)%G ==0:
                check_2[i] = 1
                num2 += 1
    #check_2로만 이루어진 경우의수 (하나는 아무것도안했을경우의수)
    pos_num_by_check_2 = 2**num2-1
    pos_num_by_check = 2**(num) - 1
    result = pos_num_by_check - pos_num_by_check_2
    print(check,check_2)
    print(result)

