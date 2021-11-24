def get_data():
    TC = int(input())
    tc_num_list = []

    for _ in range(TC):
        N = int(input())
        tc_num_list.append(N)

    return [TC, tc_num_list]

def get_prime():
    prime_check = [False] * (max_num+1)
    prime = []

    for i in range(2, max_num+1):
        if prime_check[i] == False:
            prime_check[i] = True
            prime.append(i)
            x = i*2

            while x < max_num+1:
                prime_check[x] = True
                x += i
    return prime


if __name__ == "__main__":
    TC, tc_num_list = get_data()
    max_num = max(tc_num_list)
    prime = get_prime()

    for num in tc_num_list:
        result = {}

        for p in prime:
            while True:
                if num % p == 0 and num >= p:
                    if str(p) in result.keys():
                        result[str(p)] += 1
                    else:
                        result[str(p)] = 1
                else:
                    break

                num //= p
        for key, cnt in result.items():
            print(key, cnt)

