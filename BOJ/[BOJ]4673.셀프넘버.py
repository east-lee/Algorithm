def selfNum(d):
  result = d
  for i in str(d):
    result += int(i)
  return result


check = [True]*10001

for i in range(1,10001):
  if i == 1:
    print(i)
    check[selfNum(1)] = False
  else:
    if check[i] == True:
      print(i)
    if selfNum(i)<=10000:
      check[selfNum(i)] = False
