def solution(n, k, cmd):
  answer = ''
  check = ['O'] * n
  deleted = []
  num_arr = [i for i in range(n)]

  for cmd_line in cmd:
    arr = list(map(str, cmd_line.split()))

    if arr[0] == 'U':  # 만약 틀리면 이게 범위를 넘어가는거일수도잇음 ! Checkpo
      k -= int(arr[1])
    elif arr[0] == 'D':
      k += int(arr[1])
    elif arr[0] == 'C':
      deleted.append([k, num_arr.pop(k)])  # k번째 인덱스에 있던거 실제값은 num_arr.pop(k)
      if k == (len(num_arr) - 2):
        k -= 1
    else:
      now_value = num_arr
      idx, value = deleted.pop()

      num_arr.insert(idx, value)
  for idx, value in deleted:
    check[value] = 'X'
  answer = ''.join(check)

  return answer