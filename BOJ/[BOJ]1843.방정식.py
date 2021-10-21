# 제약1. N이하의 서로다른 수
# 제약 2. N의 양의 약수인 세자연수
# 제약 3. N이하의 양의 소수

def get_prime():
    prime = []
    prime_check = [False] * (N+1)

    for i in range(N+1):
        if i<2 or prime_check[i] == True:
            continue
        prime.append(i)
        x = i * 2
        while x < N+1:
            prime_check[x] = True
            x += i
    return [prime, prime_check]

def solution_1(start_num):
    global result

    for i in range(start_num+1, N+1):
        if start_num + i <= N:
            result[0] += 1
            # print(start_num, i)
        else:
            break

def solution_3():
    global result

    for i in range(len(prime)):
        for j in range(i, len(prime)):
            sum_prime = prime[i] + prime[j]
            if sum_prime <= N and not prime_check[sum_prime]:
                result[2] +=1

def solution_2():
    global result

    visited = [False] * (N+1)
    pos_num = []
    for i in range(1, N+1):
        if visited[i]: break
        if not N % i:
            a, b = i, N // i
            visited[a], visited[b] = True, True
            pos_num.extend([a, b])

    for i in range(len(pos_num)):
        for j in range(i, len(pos_num)):
            sum_num = pos_num[i] + pos_num[j]
            if sum_num <= N and visited[sum_num]:
                result[1] += 1

if __name__ == "__main__":
    N = int(input())
    prime, prime_check = get_prime()

    result = [0,0,0]

    for i in range(1, N+1):
        solution_1(i)

    solution_2()
    solution_3()

    for r in result: print(r)