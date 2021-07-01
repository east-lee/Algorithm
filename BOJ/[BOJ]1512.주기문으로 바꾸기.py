# N보다 작거나 같은 주기문 P라고 가정
# 그럼 각각의 길이에 대해 배수 형태로 인덱스의 글자를 모으고
# 이 때 ACGT만 존재하므로 dctionary로 저장
# 가장 많이 나온 글자로 다 변환한다고 가정하면 이게 해당 주기길이에서 가장 최소로 바꾸는 것!

def main(P):
  global min_result

  result_P = 0

  for start_index in range(P):
    cnt_dict = {
      'A':0, 'C':0, 'G':0, 'T':0
    }
    total_cnt = 0
    while start_index < L:
      total_cnt += 1
      string = string_data[start_index]
      cnt_dict[string] += 1
      start_index += P
    result_P += total_cnt - max(cnt_dict.values())

  min_result = min(min_result, result_P)

def get_data():
  N = int(input())
  string_data = list(input())
  L = len(string_data)

  return [N, string_data, L]


if __name__ == "__main__":
  N, string_data, L = get_data()
  min_result = L

  for P in range(N,0,-1):
    main(P)

  print(min_result)