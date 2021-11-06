def get_data():
  data = list(map(int,input().split()))
  return [data[0], data[1:]]

def solution(num_list):
  global result

  num_list.sort(key=lambda x:-x)

  num_1, num_2 = num_list

  while num_2:
    temp = num_1 % num_2
    num_1 = num_2
    num_2 = temp
  # print(num_1)
  result += num_1


def select_num(k=-1, num_list = []):

  if len(num_list) == 2:
    solution(num_list)
    return
  for i in range(k+1, N):
    select_num(i, num_list + [arr[i]])

if __name__ == "__main__":
  TC = int(input())

  for _ in range(TC):
    result = 0
    N, arr = get_data()
    select_num()
    print(result)

