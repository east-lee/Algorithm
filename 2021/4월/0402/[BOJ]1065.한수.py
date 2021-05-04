if __name__ == "__main__":
  N = int(input())
  result = 0

  for i in range(1,N+1):
    if i <= 99:
      result += 1
    else:
      splited_list = list(map(int,str(i)))
      if splited_list[0] - splited_list[1] == splited_list[1] -splited_list[2]:
        result += 1
  print(result)