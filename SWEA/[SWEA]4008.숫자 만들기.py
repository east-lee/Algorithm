def main(operator, operand, idx, result, k, dcheck):
    global max_result, min_result

    if idx == k:
        if max_result < result: max_result = result
        if min_result > result: min_result = result
        return

    for i in range(4):
        new_operator = operator[:]
        new_result = result
        if new_operator[i]:
            new_operator[i] -=1
            check = dcheck[:]
            if i==0:
                new_result += operand[idx]
                check.append('+')
            elif i==1:
                new_result -= operand[idx]
                check.append('-')
            elif i==2:
                new_result *= operand[idx]
                check.append('*')
            else:
                new_result = int(new_result /operand[idx])
                check.append('//')
            main(new_operator,operand,idx+1,new_result,k,check)

max_result = -100000000
min_result = 100000000
if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        max_result = -100000000
        min_result = 100000000
        n = int(input())
        operator = list(map(int,input().split()))
        operand = list(map(int,input().split()))

        main(operator, operand[1:], 0, operand[0], n-1,[])
        print(f'#{t} {max_result-min_result}')