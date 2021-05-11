orderOperator = []

def solution(expression):
  global orderOperator
  DFS(0,['*','+','-'],[])

  answer = 0
  operand = []
  operator = []
  num = ''
  for i in expression:
    if i in ['*','+','-']:
      operand.append(int(num))
      operator.append(i)
      num = ''
    else: num += i
  operand.append(int(num))
  for selectedOperator in orderOperator:
    check_arr = operator[:]
    new_operand = operand[:]
    for op in selectedOperator:
      cnt = -1

      for idx,i in enumerate(check_arr):
        if i in ['*','+','-']:
          cnt += 1
        if i == op:
          check_arr[idx] = 'x'
          a = new_operand.pop(cnt)
          b = new_operand.pop(cnt)
          if op == '*': new_operand.insert(cnt,a*b)
          elif op == '+': new_operand.insert(cnt,a+b)
          else: new_operand.insert(cnt,a-b)
          cnt -=1
    if abs(new_operand[0]) > answer:
      answer = abs(new_operand[0])


  return answer



def DFS(k,arr,result):
  global orderOperator

  if k == 3:
    orderOperator.append(result)
    return
  for i in arr:
    if i not in result:
      DFS(k+1,arr,result+[i])


solution("100-200*300-500+20")
