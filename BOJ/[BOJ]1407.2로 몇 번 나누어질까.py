def solution(num):
    cnt = num
    i = 2

    while i <= num:
        cnt += (num//i) * (i // 2)
        i *= 2

    return cnt

def get_data():
    num_1, num_2 = map(int, input().split())

    return [num_1, num_2]

if __name__ == "__main__":
    num_1, num_2 = get_data()

    print(solution(num_2) - solution(num_1-1))
