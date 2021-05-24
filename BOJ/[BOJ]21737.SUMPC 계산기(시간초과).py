def main():
  global input_data
  cnt = 0
  operand, operator = [], []
  operand_append = ''
  for data in input_data:
    try:
      data = str(int(data))
      operand_append += data
    except:
      if operand_append:
        operand.append(int(operand_append))
      operand_append = ''
      operator.append(data)
      if data == 'C': cnt += 1
  if not cnt:
    print('NO OUTPUT')
    return
  operand = operand[::-1]
  for oper in operator:
    if oper == 'C':
      print(operand[-1],end = ' ')
      cnt -= 1
    else:
      x = operand.pop()
      y = operand.pop()
      operand.append(calc(x,y,oper))
    if not cnt: break

def calc(x,y,oper):
  if oper == 'S':
    return x-y
  elif oper == 'M':
    return x*y
  elif oper == 'U':
    if x < 0:
      return -(abs(x)//y)
    else: return x//y
  elif oper == 'P':
    return x + y

if __name__ == "__main__":
  N = int(input())
  input_data = list(input())

  main()