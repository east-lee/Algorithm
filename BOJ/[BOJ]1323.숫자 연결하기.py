def get_mod(num):
    return num % K

def get_data():
    N, K = map(int, input().split())

    return [N, K]


if __name__ == "__main__":
    N, K = get_data()
    pos_mod = [False] * (K)
    check_num = N
    cnt = 1
    flag = False
    while True:
        mod_num = get_mod(check_num)
        if mod_num == 0:
            flag = True
            break
        if pos_mod[mod_num]:
            break
        else:
            pos_mod[mod_num] = True
            check_num = int(str(mod_num) + str(N))
            cnt += 1

    print(cnt) if flag else print(-1)








