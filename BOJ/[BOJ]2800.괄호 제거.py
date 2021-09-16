
def dfs(k=0, remove_bracket = 0):
  global expression, result_list

  if k == len(bracket_pair):
    if remove_bracket:
      r = ''.join(expression)
      result_list.append(r)
    return

  index1, index2 = bracket_pair[k]
  expression[index1], expression[index2] = '', ''
  dfs(k+1, 1)
  expression[index1], expression[index2] = '(', ')'
  dfs(k+1, remove_bracket)

def find_bracket():
  bracket_pair = []
  bracket_stack = []
  for i in range(len(expression)):
    e = expression[i]
    if e not in ['(', ')']: continue
    elif e == '(':
      bracket_stack.append([-1, i])
    else:
      value, index = bracket_stack.pop()
      bracket_pair.append([index, i])

  return bracket_pair

if __name__ == "__main__":
  expression = list(input())
  result_list = []
  bracket_pair = find_bracket()
  dfs()
  result_list = list(set(result_list))
  result_list.sort()

  for line in result_list: print(line)