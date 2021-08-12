import sys

def calc(num1, ot, num2):

  return str(eval(num1 + operator[ot] +num2))


def dfs(operator_idx, mid_result):
  global  result

  if operator_idx == len(operator):
    result = max(result, int(mid_result))
    return

  dfs(operator_idx + 1, calc(mid_result, operator_idx, operand[operator_idx+1]))

  if operator_idx + 1 != len(operator):
    mr =  calc(operand[operator_idx + 1], operator_idx + 1 , operand[operator_idx + 2] )
    mr = calc(mid_result, operator_idx, mr)
    dfs(operator_idx + 2, mr)


def get_data():
  N = int(input())
  operand, operator = [], []

  EXP = list(input())

  for i in range(N):
    if i % 2: operator.append(EXP[i])
    else: operand.append(EXP[i])

  return [N, operand, operator]


if __name__ == "__main__":
  N, operand, operator = get_data()
  result = -sys.maxsize

  dfs(0, operand[0])
  print(result)