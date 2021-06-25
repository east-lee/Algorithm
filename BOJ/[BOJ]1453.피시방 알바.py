
def main():
  check = [0] * 101
  total_cnt = 0
  for num in hope_num:
    if check[num] == 0:
      check[num] = 1
    else:
      total_cnt += 1
  return total_cnt



def get_data():
  N = int(input())
  hope_num = list(map(int,input().split()))

  return [N, hope_num]


if __name__ == "__main__":
  N, hope_num = get_data()
  cnt = main()
  print(cnt)
