import sys

def inequality_check(index, num1, num2):
  # print(sign_list[index], num1, num2)
  if sign_list[index] == "<":
    if num1 < num2: return True
  else:
    if num1 > num2: return True
  return False

def find_num(k=-1, check_num = ""):
  global result, visited
  if k == K:
    if int(check_num) < int(result[0]): result[0] = check_num
    if int(check_num) > int(result[1]): result[1] = check_num

    return

  for i in range(10):
    if visited[i]:
      continue
    elif k == -1 or inequality_check(k, int(check_num[-1]), i):
      visited[i] = 1
      find_num(k+1, check_num + str(i))
      visited[i] = 0



def get_data():
  K = int(input())
  sign_list = list(map(str,input().split()))

  return [K, sign_list]


if __name__ == "__main__":
  K, sign_list = get_data()
  visited = [0] * 10
  result = [sys.maxsize, -sys.maxsize]
  find_num()

  print(result[1])
  print(result[0])