def main():
  LOVE_cnt = check_LOVE(my_name)
  max_name = others_name[0]
  max_num = 0

  for other in others_name:
    new_LOVE_cnt = check_LOVE(other)
    for k in range(4):
      new_LOVE_cnt[k] += LOVE_cnt[k]
    L,O,V,E = new_LOVE_cnt

    result = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100

    if result>max_num:
      max_num = result
      max_name = other

  return max_name

def check_LOVE(name):
  LOVE = [0]*4
  LOVE_check = ['L','O','V','E']

  for k in range(4):
    for name_check in name:
      if name_check == LOVE_check[k]:
        LOVE[k] += 1
  return LOVE


if __name__ == "__main__":
  my_name = list(input())
  others_name = []
  N = int(input())
  for _ in range(N):
    others_name.append(list(input()))
  others_name.sort()

  print(''.join(main()))
